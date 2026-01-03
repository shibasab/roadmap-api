# 言語バージョンアップグレード調査レポート

## 現在のバージョン状況

### Python
- **現在**: Python 3.7.3
- **Pipfile指定**: Python 3.7
- **runtime.txt指定**: python-3.7.3
- **状態**: ⚠️ **EOL（End of Life）** - 2023年6月27日にサポート終了

### Django
- **現在**: Django 2.2.10
- **状態**: ⚠️ **EOL（End of Life）** - 2022年4月11日にサポート終了

### 主要依存パッケージ

| パッケージ | 現在のバージョン | 最新バージョン | 状態 |
|-----------|----------------|--------------|------|
| djangorestframework | 3.10.3 | 3.15.x | ⚠️ 古い |
| psycopg2 | 2.8.4 | 2.9.x | ⚠️ 古い |
| django-cors-headers | 3.2.0 | 4.x | ⚠️ 古い |
| djangorestframework-simplejwt | 4.4.0 | 5.x | ⚠️ 古い |
| djangorestframework-jwt | 1.11.0 | 1.11.0 | ✅ 最新（非推奨） |
| django-rest-knox | 4.1.0 | 4.2.x | ⚠️ 古い |
| djoser | 2.0.3 | 2.2.x | ⚠️ 古い |
| dj-database-url | 0.5.0 | 2.1.x | ⚠️ 非常に古い |
| django-heroku | 0.3.1 | 0.3.1 | ✅ 最新（非推奨） |
| whitenoise | 5.0 | 6.x | ⚠️ 古い |
| gunicorn | 20.0.4 | 21.x | ⚠️ 古い |
| requests | 2.22.0 | 2.31.x | ⚠️ 古い |

## 推奨アップグレードパス

### オプション1: 段階的アップグレード（推奨）

#### Phase 1: Python 3.8 → 3.9
- **Python**: 3.7.3 → 3.9.x
- **Django**: 2.2.10 → 3.2 LTS（2024年4月までサポート）
- **メリット**: 安定性重視、段階的な移行が可能
- **リスク**: 低

#### Phase 2: Python 3.9 → 3.11
- **Python**: 3.9 → 3.11.x
- **Django**: 3.2 → 4.2 LTS（2026年4月までサポート）
- **メリット**: 長期サポート版への移行
- **リスク**: 中

#### Phase 3: Python 3.11 → 3.12
- **Python**: 3.11 → 3.12.x
- **Django**: 4.2 → 5.0（最新版）
- **メリット**: 最新機能の利用
- **リスク**: 高（破壊的変更の可能性）

### オプション2: 直接アップグレード（迅速）

#### Python 3.11 + Django 4.2 LTS
- **Python**: 3.7.3 → 3.11.x
- **Django**: 2.2.10 → 4.2 LTS
- **メリット**: 迅速なアップグレード、長期サポート
- **リスク**: 中〜高（複数の破壊的変更に対応が必要）

## 主な破壊的変更と注意点

### Django 2.2 → 3.2
1. **Python 3.8以上必須**
2. **`django.utils.six` の削除** - Python 3では不要
3. **`USE_L10N` 設定のデフォルト変更** - 明示的な設定が必要
4. **`django.contrib.postgres` の変更**
5. **`django-heroku` パッケージの非推奨化**

### Django 3.2 → 4.2
1. **Python 3.8以上必須**（推奨は3.10以上）
2. **`django.utils.translation.ugettext_lazy()` → `django.utils.translation.gettext_lazy()`**
3. **`django.conf.urls.url()` → `django.urls.re_path()`**
4. **CSRF保護の強化**
5. **`USE_TZ` のデフォルトが `True` に変更**
6. **PostgreSQL 9.6以上必須**

### Django 4.2 → 5.0
1. **Python 3.10以上必須**
2. **PostgreSQL 12以上必須**
3. **`USE_L10N` 設定の削除**
4. **`django.contrib.postgres.fields.JSONField` → `models.JSONField`**
5. **`django-heroku` パッケージの完全非推奨**

## 依存パッケージの互換性

### 互換性確認が必要なパッケージ

1. **djangorestframework-jwt** (1.11.0)
   - ⚠️ **非推奨パッケージ**
   - 代替: `djangorestframework-simplejwt`（既にインストール済み）
   - 移行が必要

2. **django-heroku** (0.3.1)
   - ⚠️ **非推奨パッケージ**（Django 4.0以降）
   - 代替: 手動設定または `django-on-heroku` などの代替パッケージ
   - 移行が必要

3. **dj-database-url** (0.5.0)
   - ⚠️ **非常に古いバージョン**
   - 最新版（2.1.x）への更新が必要
   - 互換性の問題が発生する可能性あり

4. **psycopg2** (2.8.4)
   - 最新版（2.9.x）への更新が必要
   - Python 3.12対応のため

## コードベースの確認事項

### 確認結果

#### ✅ 問題なし
1. **settings.py**
   - `USE_L10N = True` - 既に設定済み ✅
   - `USE_TZ = True` - 既に設定済み ✅
   - URL設定は `django.urls.path` を使用（問題なし）✅

2. **モデル定義**
   - PostgreSQL固有のフィールド（JSONField、ArrayField等）は使用されていない ✅
   - 標準的なDjangoモデルフィールドのみ使用 ✅

3. **認証システム**
   - `djangorestframework-jwt` は **実際には使用されていない** ✅
   - 認証には `knox` を使用（`djangorestframework-simplejwt` もインストール済みだが未使用）✅
   - `requirements.txt` から削除可能 ✅

#### ⚠️ 対応が必要
1. **settings.py**
   - `django-heroku` の使用（179行目）
   - Django 4.0以降では非推奨のため、代替設定が必要

2. **依存パッケージ**
   - `djangorestframework-jwt` - 使用されていないが、requirements.txtに含まれている（削除推奨）
   - `djangorestframework-simplejwt` - インストール済みだが未使用（削除可能）

3. **その他**
   - `dj-database-url` のバージョンが非常に古い（0.5.0 → 2.1.x）
   - 複数のパッケージが古いバージョンのまま

## 推奨アクションプラン

### ステップ1: 現状のバックアップとテスト環境の準備
- [ ] 現在のコードベースのバックアップ
- [ ] テスト環境の構築
- [ ] 既存のテストスイートの実行と結果の記録

### ステップ2: Python 3.9 + Django 3.2への移行
- [ ] `runtime.txt` を `python-3.9.x` に更新
- [ ] `Pipfile` の `python_version` を `"3.9"` に更新
- [ ] Django を 3.2 LTS に更新
- [ ] 依存パッケージの互換バージョンに更新
- [ ] コードの修正（破壊的変更への対応）
- [ ] テストの実行と修正

### ステップ3: Python 3.11 + Django 4.2 LTSへの移行
- [ ] `runtime.txt` を `python-3.11.x` に更新
- [ ] `Pipfile` の `python_version` を `"3.11"` に更新
- [ ] Django を 4.2 LTS に更新
- [ ] 依存パッケージの更新
- [ ] `django-heroku` の削除と代替設定（`settings.py` 179行目）
- [ ] `djangorestframework-jwt` の削除（未使用のため）
- [ ] `dj-database-url` を 2.1.x に更新
- [ ] コードの修正
- [ ] テストの実行と修正

### ステップ4: 最新版への移行（オプション）
- [ ] Python 3.12 + Django 5.0への移行検討
- [ ] パフォーマンステスト
- [ ] セキュリティ監査

## リスク評価

| リスク | レベル | 対策 |
|--------|--------|------|
| 破壊的変更による機能停止 | 中 | 段階的移行、十分なテスト |
| 依存パッケージの互換性問題 | 中 | 各パッケージの互換性マトリックス確認 |
| パフォーマンスの劣化 | 低 | ベンチマークテストの実施 |
| セキュリティ問題 | 低 | 最新版への移行で改善 |

## 参考資料

- [Django リリースノート](https://docs.djangoproject.com/en/stable/releases/)
- [Python リリーススケジュール](https://www.python.org/dev/peps/pep-0602/)
- [Django アップグレードガイド](https://docs.djangoproject.com/en/stable/howto/upgrade-version/)
- [Django REST Framework リリースノート](https://www.django-rest-framework.org/community/3.14-announcement/)

## 具体的な修正が必要な箇所

### 1. settings.py の修正（Django 4.0以降）

**現在のコード（179-180行目）:**
```python
if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']
    import django_heroku
    django_heroku.settings(locals())
```

**修正案（django-heroku の代替）:**
```python
if not DEBUG:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
    # django-heroku の代替設定
    import dj_database_url
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
    # その他のHeroku固有設定
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```

### 2. requirements.txt の整理

**削除推奨:**
- `djangorestframework-jwt==1.11.0` （未使用）

**更新が必要:**
- `dj-database-url==0.5.0` → `dj-database-url>=2.1.0`
- その他のパッケージも最新の互換バージョンに更新

### 3. Pipfile の更新

**更新が必要なパッケージ:**
```toml
[packages]
django = ">=4.2,<5.0"  # 2.2.10 → 4.2 LTS
djangorestframework = ">=3.14.0"
dj-database-url = ">=2.1.0"  # 0.5.0 → 2.1.0
# その他のパッケージも更新
```

## 次のステップ

1. ✅ この調査レポートをレビュー
2. アップグレードパスの決定（オプション1または2）
3. テスト環境での検証開始
4. 段階的な移行の実施
5. `django-heroku` の代替設定の実装
6. 未使用パッケージの削除
