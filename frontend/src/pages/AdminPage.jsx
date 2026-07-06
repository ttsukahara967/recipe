import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  createRecipe,
  deleteRecipe,
  getRecipes,
  updateRecipe,
} from "../api";

const PAGE_SIZE = 10;
const emptyForm = { title: "", description: "", ingredients: "", steps: "" };

function AdminPage() {
  const [recipes, setRecipes] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [form, setForm] = useState(emptyForm);
  const [editingId, setEditingId] = useState(null);
  const [error, setError] = useState(null);

  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));

  const loadRecipes = () => {
    getRecipes({ page, pageSize: PAGE_SIZE })
      .then((data) => {
        setRecipes(data.items);
        setTotal(data.total);
      })
      .catch((err) => setError(err.message));
  };

  useEffect(() => {
    loadRecipes();
  }, [page]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingId) {
        await updateRecipe(editingId, form);
      } else {
        await createRecipe(form);
      }
      setForm(emptyForm);
      setEditingId(null);
      loadRecipes();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleEdit = (recipe) => {
    setEditingId(recipe.id);
    setForm({
      title: recipe.title,
      description: recipe.description || "",
      ingredients: recipe.ingredients || "",
      steps: recipe.steps || "",
    });
  };

  const handleCancelEdit = () => {
    setEditingId(null);
    setForm(emptyForm);
  };

  const handleDelete = async (id) => {
    if (!window.confirm("削除しますか？")) return;
    try {
      await deleteRecipe(id);
      if (editingId === id) handleCancelEdit();
      loadRecipes();
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="container">
      <Link to="/">← レシピ一覧へ戻る</Link>

      <h1>レシピ管理（管理者用）</h1>

      {error && <p className="error">{error}</p>}

      <form onSubmit={handleSubmit} className="recipe-form">
        <input
          name="title"
          placeholder="料理名"
          value={form.title}
          onChange={handleChange}
          required
        />
        <textarea
          name="description"
          placeholder="説明"
          value={form.description}
          onChange={handleChange}
        />
        <textarea
          name="ingredients"
          placeholder="材料"
          value={form.ingredients}
          onChange={handleChange}
        />
        <textarea
          name="steps"
          placeholder="手順"
          value={form.steps}
          onChange={handleChange}
        />
        <div className="form-actions">
          <button type="submit">{editingId ? "更新" : "登録"}</button>
          {editingId && (
            <button type="button" onClick={handleCancelEdit}>
              キャンセル
            </button>
          )}
        </div>
      </form>

      <ul className="recipe-list">
        {recipes.map((recipe) => (
          <li key={recipe.id} className="recipe-item">
            <h2>{recipe.title}</h2>
            <p>{recipe.description}</p>
            <pre>{recipe.ingredients}</pre>
            <pre>{recipe.steps}</pre>
            <div className="item-actions">
              <button onClick={() => handleEdit(recipe)}>編集</button>
              <button onClick={() => handleDelete(recipe.id)}>削除</button>
            </div>
          </li>
        ))}
      </ul>

      <div className="pagination">
        <button disabled={page <= 1} onClick={() => setPage((p) => p - 1)}>
          前へ
        </button>
        <span>
          {page} / {totalPages}
        </span>
        <button
          disabled={page >= totalPages}
          onClick={() => setPage((p) => p + 1)}
        >
          次へ
        </button>
      </div>
    </div>
  );
}

export default AdminPage;
