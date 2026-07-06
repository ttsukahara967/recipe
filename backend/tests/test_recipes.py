def test_list_recipes_empty(client):
    res = client.get("/api/recipes/")
    assert res.status_code == 200
    assert res.json() == {"items": [], "total": 0, "page": 1, "page_size": 10}


def test_list_recipes_returns_seeded_data_desc_by_id(client, seed_recipes):
    res = client.get("/api/recipes/")
    assert res.status_code == 200
    data = res.json()
    assert data["total"] == 3
    assert [item["id"] for item in data["items"]] == list(reversed(seed_recipes))


def test_list_recipes_pagination(client):
    for i in range(12):
        client.post("/api/recipes/", json={"title": f"レシピ{i}"})

    res = client.get("/api/recipes/", params={"page": 2, "page_size": 10})
    data = res.json()
    assert data["total"] == 12
    assert data["page"] == 2
    assert data["page_size"] == 10
    assert len(data["items"]) == 2


def test_search_recipes_by_keyword(client, seed_recipes):
    res = client.get("/api/recipes/", params={"q": "じゃがいも"})
    data = res.json()
    titles = {item["title"] for item in data["items"]}
    assert titles == {"カレーライス", "肉じゃが"}


def test_search_recipes_no_match(client, seed_recipes):
    res = client.get("/api/recipes/", params={"q": "存在しない食材"})
    data = res.json()
    assert data["items"] == []
    assert data["total"] == 0


def test_create_recipe(client):
    payload = {
        "title": "オムライス",
        "description": "卵とご飯",
        "ingredients": "卵, ご飯, ケチャップ",
        "steps": "チキンライスを作って卵で包む",
    }
    res = client.post("/api/recipes/", json=payload)
    assert res.status_code == 201
    data = res.json()
    assert data["title"] == payload["title"]
    assert "id" in data


def test_get_recipe(client, seed_recipes):
    recipe_id = seed_recipes[0]
    res = client.get(f"/api/recipes/{recipe_id}")
    assert res.status_code == 200
    assert res.json()["id"] == recipe_id


def test_get_recipe_not_found(client):
    res = client.get("/api/recipes/99999")
    assert res.status_code == 404


def test_update_recipe(client, seed_recipes):
    recipe_id = seed_recipes[0]
    payload = {
        "title": "カレーライス(改)",
        "description": "スパイスを追加",
        "ingredients": "じゃがいも, 玉ねぎ, スパイス",
        "steps": "煮込んでスパイスを加える",
    }
    res = client.put(f"/api/recipes/{recipe_id}", json=payload)
    assert res.status_code == 200
    assert res.json()["title"] == "カレーライス(改)"


def test_update_recipe_not_found(client):
    res = client.put("/api/recipes/99999", json={"title": "存在しない"})
    assert res.status_code == 404


def test_delete_recipe(client, seed_recipes):
    recipe_id = seed_recipes[0]
    res = client.delete(f"/api/recipes/{recipe_id}")
    assert res.status_code == 204

    res = client.get(f"/api/recipes/{recipe_id}")
    assert res.status_code == 404


def test_delete_recipe_not_found(client):
    res = client.delete("/api/recipes/99999")
    assert res.status_code == 404
