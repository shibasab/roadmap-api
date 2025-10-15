## OpenAPI ドキュメント生成（drf-spectacular）

このリポジトリは Django + DRF 構成です。OpenAPI スキーマは drf-spectacular により自動生成・配信できます。

### 依存のインストール
```bash
python3 -m pip install -r requirements.txt
# もし drf-spectacular が未導入の場合のみ
python3 -m pip install drf-spectacular "drf-spectacular[sidecar]"
```

### ドキュメント UI（ブラウザ）
開発サーバ起動後、以下にアクセスしてください。
- `/api/schema/`（OpenAPI JSON）
- `/api/docs/`（Swagger UI）
- `/api/redoc/`（Redoc）

### スキーマファイルの生成（静的出力）
CI 等で成果物として保存する場合は次のコマンドで生成します。

```bash
# SECRET_KEY が必須（本番以外の一時値でOK）
export SECRET_KEY=dev

python3 manage.py spectacular --file openapi.yaml
python3 manage.py spectacular --format openapi-json --file openapi.json
```

生成された `openapi.yaml` / `openapi.json` はリポジトリ直下に出力されます。出力先は `--file` で任意パスに変更可能です。

### 注意事項
- このプロジェクトでは `DEBUG=False` 設定のため、管理コマンド実行時にも `SECRET_KEY` が未設定だと起動できません。上記のように一時値を `export` してください。
- Swagger/Redoc の UI アセットは `drf-spectacular[sidecar]` で提供されます。環境により追加インストールが必要な場合があります。
- スキーマはビューやシリアライザの変更に追従します。API 変更時は再生成してください。