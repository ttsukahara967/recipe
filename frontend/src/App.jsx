import { Route, Routes } from "react-router-dom";
import RecipeList from "./pages/RecipeList.jsx";
import AdminPage from "./pages/AdminPage.jsx";

function App() {
  return (
    <Routes>
      <Route path="/" element={<RecipeList />} />
      <Route path="/admin" element={<AdminPage />} />
    </Routes>
  );
}

export default App;
