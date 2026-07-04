import { useEffect, useState } from "react";
import { createRecipe, deleteRecipe, getRecipes } from "./api";

const emptyForm = { title: "", description: "", ingredients: "", steps: "" };

function App() {
  const [recipes, setRecipes] = useState([]);
  const [form, setForm] = useState(emptyForm);
  const [error, setError] = useState(null);

  const loadRecipes = () => {
    getRecipes()
      .then(setRecipes)
      .catch((err) => setError(err.message));
  };

  useEffect(() => {
    loadRecipes();
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await createRecipe(form);
      setForm(emptyForm);
      loadRecipes();
    } catch (err) {
      setError(err.message);
    }
  };

  const handleDelete = async (id) => {
    try {
      await deleteRecipe(id);
      loadRecipes();
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div className="container">
      <h1>レシピ管理システム</h1>

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
        <button type="submit">登録</button>
      </form>

      <ul className="recipe-list">
        {recipes.map((recipe) => (
          <li key={recipe.id} className="recipe-item">
            <h2>{recipe.title}</h2>
            <p>{recipe.description}</p>
            <pre>{recipe.ingredients}</pre>
            <pre>{recipe.steps}</pre>
            <button onClick={() => handleDelete(recipe.id)}>削除</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
