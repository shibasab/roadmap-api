# API 一覧

このプロジェクトの公開API、エンドポイント、シリアライザ、モデルの概要と各モジュール詳細へのリンクを示します。

## エンドポイント構成

- ルート: `/api/v1/` → `apiv1`
- ルート: `/api/accounts/` → `accounts`

## クイックリンク

- [apiv1 の詳細](api/apiv1.md)
- [accounts の詳細](api/accounts.md)

## 起動と利用例

- 開発サーバ起動:
  ```bash
  python manage.py runserver
  ```
- 認証（Knox）
  - ヘッダ: `Authorization: Token <token>`
  - 発行: `/api/accounts/auth/register` または `/api/accounts/auth/login`

## スキーマ/型について

- `apiv1.serializers.RoadmapParentSerializer` は `roadmap` 配列のネスト作成をサポートします
- `accounts` は Django 標準 `User` を使用します
