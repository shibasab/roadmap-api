# accounts API ドキュメント

## エンドポイント

- POST /api/accounts/auth/register
  - 概要: ユーザ登録し、トークンを返却
  - リクエストボディ:
    ```json
    {"username":"alice","email":"a@example.com","password":"secret"}
    ```
  - レスポンス例:
    ```json
    {"user":{"id":1,"username":"alice","is_superuser":false},"token":"<token>"}
    ```
  - 例:
    ```bash
    curl -X POST http://localhost:8000/api/accounts/auth/register \
      -H 'Content-Type: application/json' \
      -d '{"username":"alice","email":"a@example.com","password":"secret"}'
    ```

- POST /api/accounts/auth/login
  - 概要: ログインしてトークンを返却
  - リクエストボディ:
    ```json
    {"username":"alice","password":"secret"}
    ```
  - レスポンス例: register と同様

- GET /api/accounts/auth/user
  - 概要: 認証済ユーザ情報を返却
  - 認証: Knox Token (`Authorization: Token <token>`) 必須
  - 例:
    ```bash
    curl -H 'Authorization: Token <token>' http://localhost:8000/api/accounts/auth/user
    ```

- POST /api/accounts/auth/logout
  - 概要: ログアウト（トークン無効化）
  - 認証: Knox Token 必須

## ビュー

### RegisterAPIView (POST)
- `RegisterSerializer` を用いユーザを作成し `AuthToken` を返却

### LoginAPIView (POST)
- `LoginSerializer` により認証し `AuthToken` を返却

### UserAPIView (GET)
- `IsAuthenticated` 必須、現在のユーザを返却

## シリアライザ

### UserSerializer
- フィールド: `id`, `username`, `is_superuser`

### RegisterSerializer
- 入力: `username`, `email`, `password(write_only)`
- create: `User.objects.create_user(...)`

### LoginSerializer
- 入力: `username`, `password`
- validate: `authenticate(**data)` で検証、失敗時 ValidationError
