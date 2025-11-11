# Agent Onboarding Guide – CNP TCG 音楽制作プロジェクト

## 初動指示
- セッション開始直後に必ず本ファイル `AGENTS.md` を開き、最新の運用ルールと初期読込フローを確認する。
- 以下の初期読込フローを完了させるまでタスク着手を保留し、参照ファイルの変更有無を毎回チェックする。

## ミッション概要
- **目的**: CNPトレーディングカードゲーム（CNP TCG）の世界観を音楽・物語双方から表現する。
- **コア成果物**: Suno用プロンプト、生成楽曲音源、世界観考察記事、カードデータ分析。
- **キーワード**: 「敗北が糧となる世界」／四大陸（アクアノーヴァ・カグツチ・メテオラス・ミッドガン）／セイドウ組織。

## 初期読込フロー（必ず順番に確認）
1. `docs/lore/CNP_TCG_STORY_ANALYSIS.md`
   - 公式情報とカード全体の分析。世界観理解の土台。
2. `data/cards.json`
   - 198枚のカードデータ。フレーバーテキスト根拠を検索するために使用。
3. `docs/world-analysis/README.md`
   - 考察記事の運用ルールを確認。続けて `docs/world-analysis/articles/*.md` を順番に熟読。
4. `prompts/templates/SUNO_MUSIC_PROMPT_TEMPLATE.md`
   - Sunoプロンプト作成時の必須テンプレート。
5. `prompts/suno/四界解放譜/*.md`
   - 既存楽曲の完成プロンプト。構成・語彙・根拠の参照元。
6. `audio/README.md` と `audio/leon-album-1-shikai-kaihoufu/`
   - 音源命名規則と完成ファイルの配置状況を把握。

## ディレクトリマップ
- `audio/` : 生成済み楽曲と関連アートワーク。`README.md` に命名規則あり。
- `data/` : 構造化データ。現状は `cards.json` のみ。
- `docs/lore/` : 世界観の一次資料（公式情報整理）。
- `docs/world-analysis/` : 考察記事・画像・執筆テンプレート。
- `prompts/suno/` : Sunoへ渡す最終プロンプトをアルバム単位で保存。
- `prompts/templates/` : 新規プロンプト作成時に埋めるテンプレート群。

## 作業ワークフロー
### Suno楽曲制作
1. テンプレートに沿って要件定義（`prompts/templates/`）。
2. `data/cards.json` と `docs/lore/...` から根拠抽出。
3. 歌詞・構成・アレンジを記述したプロンプトを `prompts/suno/<アルバム>/` に保存。
4. Sunoで生成した音源は `audio/<アルバム名>/` へ配置し、`audio/README.md` の命名規則を順守。

### 世界観考察記事
1. `docs/world-analysis/prompts/` のテンプレートで構成を作成。
2. 事実と仮説を明確にラベル分け（本文内で `(事実)` `(仮説)` など）。
3. 引用カードは `(BT1-11)` のようにカードIDを併記。
4. 完成記事は `docs/world-analysis/articles/` に日付スラッグ形式で保存。

## 設計・記法の原則
- **カード根拠**: 必ずカードID/名称/要約を明記。`data/cards.json` から抜粋。
- **用語整合**: 公式呼称（例: 「三種の神器」「テンシュ」）を使用し、俗称は括弧内補足。
- **言語**: 日本語主体、必要に応じて英語タグを追加（Sunoの指示に準拠）。
- **ファイル形式**: Markdown（UTF-8, ASCIIベース）を基本とし、画像は `docs/world-analysis/picture/` に配置。

## 出力先と命名規則
- **プロンプト**: `prompts/suno/<企画名>/YYYYMMDD_<slug>.md` を推奨。既存例は `四界解放譜/`。
- **Codexエージェント命名**: Codexが作成するSunoプロンプトファイルは、必ずファイル名に`codex`を含める（例: `YYYYMMDD_<slug>_codex.md`）。保存先が`prompts/suno/2nd_works/`の場合も同様。
- **音源**: `audio/<アルバム>/[トラック番号]_[曲名]_[バージョン].wav`（`audio/README.md` 参照）。
- **考察記事**: `docs/world-analysis/articles/YYYY-MM-DD_<slug>.md`。

## 補足
- すべての応答は原則として日本語で行うこと。必要に応じて英語タグや専門用語を補足する場合でも、日本語説明を併記する。
- 追加リソースは必ずこのファイルで導線を更新すること。
- 新企画を起こす際は `prompts/suno/` に新ディレクトリを作成し、`README.md` のフォルダ構成も合わせて更新。
- Sunoプロンプトを作成・更新する際は必ず `prompts/templates/SUNO_MUSIC_PROMPT_TEMPLATE.md` のセクション別声質メタタグルールを確認し、歌詞の全セクションに指定を付ける。
- 不明点があれば、まず `docs/lore/CNP_TCG_STORY_ANALYSIS.md` 内のToDoリストや未解決謎を参照し、優先タスクを判断すること。
