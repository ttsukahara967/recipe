import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getRecipes } from "../api";

const PAGE_SIZE = 10;

function RecipeList() {
  const [recipes, setRecipes] = useState([]);
  const [total, setTotal] = useState(0);
  const [page, setPage] = useState(1);
  const [searchInput, setSearchInput] = useState("");
  const [query, setQuery] = useState("");
  const [error, setError] = useState(null);

  const totalPages = Math.max(1, Math.ceil(total / PAGE_SIZE));

  useEffect(() => {
    getRecipes({ page, pageSize: PAGE_SIZE, q: query })
      .then((data) => {
        setRecipes(data.items);
        setTotal(data.total);
      })
      .catch((err) => setError(err.message));
  }, [page, query]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    setPage(1);
    setQuery(searchInput);
  };

  return (
    <div className="container">
      <Link to="/admin" className="admin-link">
        管理者用
      </Link>

      <h1>レシピ管理システム</h1>

      {error && <p className="error">{error}</p>}

      <form onSubmit={handleSearchSubmit} className="search-form">
        <input
          placeholder="レシピを検索"
          value={searchInput}
          onChange={(e) => setSearchInput(e.target.value)}
        />
        <button type="submit">検索</button>
      </form>

      <ul className="recipe-list">
        {recipes.map((recipe) => (
          <li key={recipe.id} className="recipe-item">
            <h2>{recipe.title}</h2>
            <p>{recipe.description}</p>
            <pre>{recipe.ingredients}</pre>
            <pre>{recipe.steps}</pre>
          </li>
        ))}
        {recipes.length === 0 && <p>レシピが見つかりませんでした。</p>}
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

export default RecipeList;
