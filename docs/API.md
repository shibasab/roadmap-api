# API リファレンス（OpenAPI）

このプロジェクトの API は OpenAPI で提供されます。以下からブラウザ UI または機械可読形式で参照できます。

## 参照リンク

- Swagger UI: `/swagger/`
- Redoc: `/redoc/`
- OpenAPI JSON/YAML: `/openapi.json`, `/openapi.yaml`

## ローカルでの利用

```bash
python manage.py runserver
# ブラウザで http://localhost:8000/swagger/ にアクセス
```

## 認証

- Knox トークンを使用します。ヘッダに `Authorization: Token <token>` を付与してください。

## 静的スキーマ

- リポジトリには `docs/openapi.yaml` も同梱しています。
