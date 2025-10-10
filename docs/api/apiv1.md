# apiv1 API ドキュメント

## エンドポイント

- GET /api/v1/roadmaps/
  - 概要: 親ロードマップ一覧を取得
  - レスポンス: `RoadmapParentListSerializer[]`
  - 例:
    ```bash
    curl -s http://localhost:8000/api/v1/roadmaps/
    ```

- POST /api/v1/roadmaps/
  - 概要: 親ロードマップと子ロードマップ群を作成
  - リクエストボディ: `RoadmapParentSerializer`
  - 例:
    ```bash
    curl -X POST http://localhost:8000/api/v1/roadmaps/ \
      -H 'Content-Type: application/json' \
      -d '{
            "title": "Python入門",
            "overview": "初学者向け",
            "roadmap": [
              {"title": "基礎文法", "detail": "if/for/関数", "next_id": null},
              {"title": "標準ライブラリ", "detail": "collections 等", "next_id": null}
            ]
          }'
    ```

- GET /api/v1/roadmaps/<uuid:pk>
  - 概要: 指定親ロードマップの詳細を取得
  - レスポンス: `RoadmapParentSerializer`
  - 例:
    ```bash
    curl -s http://localhost:8000/api/v1/roadmaps/4fa0a1f0-0000-0000-0000-000000000000
    ```

- PUT /api/v1/roadmaps/<uuid:pk>
  - 概要: 親ロードマップを更新（子含む）
  - リクエストボディ: `RoadmapParentSerializer`

- DELETE /api/v1/roadmaps/<uuid:pk>
  - 概要: 親ロードマップを削除

## ビュー

### RoadmapParentView (GET, POST)
- GET: 親ロードマップ一覧を `RoadmapParentListSerializer` で返却
- POST: `RoadmapParentSerializer` でネスト作成

### RoadmapDetail (GET, PUT, DELETE)
- GET/PUT/DELETE: `pk` に対応する `RoadmapParent` を対象

## シリアライザ

### RoadmapSerializer
- フィールド: `id (read-only)`, `title`, `detail`, `next_id`

### RoadmapParentSerializer (WritableNestedModelSerializer)
- フィールド: `id (read-only)`, `title`, `overview`, `like`, `created_at (read-only)`, `roadmap (RoadmapSerializer[])`
- create: ネストされた `roadmap` をまとめて作成

### RoadmapParentListSerializer
- フィールド: `id (read-only)`, `title`, `overview`, `like`, `created_at (read-only)`

## モデル

### RoadmapParent
- `id: UUID (PK)`
- `title: Char(50)`
- `overview: Char(200)`
- `like: Integer (default 0)`
- `created_at: DateTime`

### Roadmap
- `id: UUID (PK)`
- `title: Char(50)`
- `detail: Char(200)`
- `created_at: DateTime`
- `next_id: UUID (nullable)`
- `parent: FK -> RoadmapParent (related_name='roadmap')`
