# レシピ管理システム（骨組み）

- フロント: React (Vite)
- バックエンド: FastAPI
- DB: MySQL
- 環境: Docker Compose

## 起動方法

```bash
docker compose up --build
```

- フロントエンド: http://localhost:5173
- バックエンドAPI: http://localhost:8000
- APIドキュメント: http://localhost:8000/docs

## 構成

```
recipe/
├── backend/        # FastAPI
│   └── app/
│       ├── main.py
│       ├── db/         # DB接続
│       ├── models/     # SQLAlchemyモデル
│       ├── schemas/    # Pydanticスキーマ
│       ├── crud/       # DB操作
│       └── routers/    # APIエンドポイント
├── frontend/       # React (Vite)
│   └── src/
├── docker-compose.yml
```

## 実装済みAPI（レシピCRUD）

- `GET /api/recipes/` 一覧取得
- `GET /api/recipes/{id}` 詳細取得
- `POST /api/recipes/` 新規作成
- `PUT /api/recipes/{id}` 更新
- `DELETE /api/recipes/{id}` 削除

まだ骨組みのみのため、認証・画像アップロード・カテゴリ分けなどは未実装です。
