# CNP TCG 楽曲カバーアート制作ワークフロー

*作成日: 2026-01-07*
*対象: Midjourney v6使用*

---

## 🎯 このワークフローの目的

CNP TCG音楽プロジェクトの各楽曲に対応するカバーアートをMidjourneyで制作するための標準手順書です。

---

## 📋 制作フロー（ステップバイステップ）

### ステップ1: 楽曲情報の把握

以下の情報を確認・整理します：

1. **楽曲タイトル**（日本語・英語）
2. **楽曲種類**（OP/ED/ソロ/ユニット/テーマ曲等）
3. **担当キャラクター**（該当する場合）
4. **ジャンル・音楽スタイル**
5. **歌詞の主要テーマ・感情**
6. **カード根拠**（キャラクター設定・世界観）

**確認元**:
- Sunoプロンプトファイル（`prompts/suno/`）
- 日本語歌詞版セクション
- カードデータ（`data/cards.json`）

---

### ステップ2: ビジュアルコンセプトの決定

#### **2-1. キャラクター設定の抽出**

歌詞とカード情報から以下を決定：

- **外見**: 髪色、目の色、服装、アクセサリー
- **表情**: 主要な感情（儚い、決意、喜び、葛藤等）
- **ポーズ**: バストアップ、全身、グループ等
- **象徴的要素**: キャラクター固有のモチーフ（炎、水、森、宇宙等）

#### **2-2. カラーパレットの選定**

楽曲の雰囲気に合わせて：

- **明るい希望系**: ゴールド、シアン、ホワイト、虹色
- **暗い葛藤系**: グレー、インディゴ、ダークブラウン、控えめな炎
- **ユニット系**: 5色（ピンク、ブルー、レッド、グリーン、イエロー/パープル）

#### **2-3. ライティング・雰囲気**

- **ドラマティック**: 強いコントラスト、リムライト
- **儚い・柔らか**: ソフトフォーカス、淡い光
- **力強い**: 下からのライティング、ネオンアクセント

---

### ステップ3: Midjourneyプロンプトの作成

#### **3-1. ベース構造**

```
[スタイル指定] + [構図] + [キャラクター詳細] + [表情・ポーズ] + [ライティング] + [背景] + [カラー遷移] + [アートスタイル] + [エフェクト] + [ムード] + [パラメータ]
```

#### **3-2. 必須要素**

✅ `anime-style` - アニメスタイル指定
✅ 構図指定（`bust-up portrait`, `group shot`, `extreme close-up`等）
✅ キャラクター詳細（外見、服装、表情）
✅ ライティング指定
✅ 背景・世界観要素
✅ `clean cel-shaded anime style` - セルシェード
✅ `--ar 1:1 --style raw --niji 6` - パラメータ

#### **3-3. スタイル統一のための参考プロンプト**

**過去の成功例を参考にタッチを統一**:

##### **例1: グループ・希望系（手を繋いで、希望の光等）**
```
anime-style ethereal composition, group of 5 girls bathed in transparent divine light, delicate fairy-like atmosphere, soft prism colors (Pink, Blue, Red, Green, Yellow) blending harmoniously like watercolors, glittering particles and bioluminescent flowers floating around, expressions of pure joy and innocent hope, translucent crystal wings or aura on their backs, dreamy soft focus background with aurora borealis and digital sparkles, high detail on sparkling eyes, transition from soft darkness to brilliant iridescent light, kawaii aesthetic clean line art with soft texture, magical and elegant, hyperpop elements presented as glittering digital dust, --ar 1:1 --style raw --niji 6
```

##### **例2: グループ・力強い系（虹色のハーモニー等）**
```
anime-style vibrant composition, dynamic low-angle group shot of 5 anime girls (Red, Blue, Green, Yellow, Purple themes) standing together looking up at a blinding ray of divine hope, central focus on the leader reaching hand towards the light, expressions of fierce determination and tearful joy, dramatic neon gold and pure white lighting cutting through heavy obsidian darkness, background showing shattering dark crystal walls revealing a brilliant sunrise, transition from deep shadow to blinding radiance symbolizing triumph, clean cel-shaded anime style with high detail on eyes and emotional expressions, sparkle effects and digital glitch particles mixing with magical aura, holographic musical note patterns, mood of epic unity and overcoming adversity, hyperpop visual aesthetic meets emotional anthem, vivid saturated colors with digital sheen, --ar 1:1 --style raw --niji 6
```

##### **例3: ソロ・希望系（ミライソロ、リサソロ等）**
```
anime-style uplifting composition, extreme close-up of hopeful teenage girl's face in foreground taking up 70% of frame with gentle yet determined eyes gradually building to radiant hope, delicate features with soft expression, tear streaks transforming into golden light particles, dramatic golden yellow and cyan lighting from side creating vibrant contrast symbolizing hope and technology, background showing silhouette of futuristic cityscape with neon lights and digital grid patterns, floating holographic interfaces and light beams, transition from dark shadowy tones (left) to brilliant golden yellow light rays (right) symbolizing journey from darkness to hope, clean cel-shaded anime style with high detail on face showing emotional journey from vulnerability to courage, light particles and digital glow effects, chromatic aberration on light elements, lens flare and bokeh effects, mood of hope determination and inner strength, girl crush K-Pop visual meets synthwave cyberpunk aesthetic, digital future meets emotional warmth, --ar 1:1 --style raw --niji 6
```

##### **例4: ソロ・儚い/葛藤系（ツミカソロ等）**
```
anime-style dark melancholic composition, bust-up portrait of fragile shrine maiden girl in center frame showing upper body and face with sorrowful amber eyes showing vulnerability and quiet sadness, delicate pale features with long flowing dark brown hair cascading down shoulders, wearing traditional white and charcoal grey miko outfit with tattered hem suggesting hardship, one hand gently touching her own cheek in self-doubt while other hand loosely holding ofuda paper charm, downcast gaze with tears forming but not falling, dramatic soft grey and shadow indigo lighting from below creating ephemeral atmosphere with gentle rim lighting, background showing massive flame god deity bound by dark ominous chains with dying sacred flames flickering weakly in distance, volcanic Kagutsuchi landscape shrouded in ash and mist with fading ember particles, transition from cold lonely shadow tones (left) to dim amber fire glow (right) symbolizing fleeting determination, clean cel-shaded anime style with high detail on sorrowful expression and delicate posture showing emotional fragility and isolation, small flame spark effects dissolving into smoke and industrial metallic ash particles gently falling around her mixing with sacred rope patterns on sleeves, chromatic aberration on fading fire elements, dark synth aesthetic with faint glowing seal marks visible on neck and hands, mood of melancholic loneliness and quiet desperation, electro-rock visual aesthetic meets Kagutsuchi shrine mythology, heavily desaturated cool-toned colors with minimal warm accents creating somber ephemeral atmosphere, whispered fragile power visualized as dying embers barely staying lit, --ar 1:1 --style raw --niji 6
```

---

### ステップ4: 歌詞からの要素抽出テンプレート

楽曲の日本語歌詞を分析し、以下を抽出：

#### **感情・ムード**
- キーワード抽出（例: 儚い、決意、希望、葛藤、喜び）
- 表情への反映

#### **象徴的フレーズ**
- 視覚化できる比喩表現（例: 「静かな炎」→ dying embers）
- 背景やエフェクトに反映

#### **カラーヒント**
- 歌詞中の色表現（例: 「赤い青い黄緑紫」→ 5色のテーマ）
- 大陸テーマカラー（アクアノーヴァ=青、カグツチ=赤等）

#### **ストーリー要素**
- 具体的な状況描写（例: 「ナルカミたちには断られた」→ 孤独感）

**歌詞例（ツミカソロ「静かな炎」）**:
```
静かに... 燃える...
誰も気づかない... 炎...

言葉少ない私は影に隠れる
人の前では何も言えなくて
でも心の奥で炎が揺れて
守りたいもののために戦う

（中略）

「私は... 弱い...」
「人と話すのも... 怖い...」
「でも...」
「守りたいものがある...」
「炎神を... 竜人たちを...」
「この炎で... 守ってみせる！」
```

**抽出結果**:
- **ムード**: 儚い、孤独、静かな決意
- **象徴**: 静かに燃える炎、影、内なる炎
- **表情**: 伏し目がち、涙が溢れそう、自己不信
- **カラー**: 赤みを抑えた暗い色調、かすかな炎の光
- **背景**: 炎神、鎖、火山、灰

---

### ステップ5: プロンプト最適化

#### **調整ポイント**

1. **文字数**: 適度な長さ（長すぎず短すぎず、500-700語程度）
2. **具体性**: 曖昧な表現を避ける
   - ❌ `beautiful` → ✅ `delicate pale features`
3. **カラー指定**: 明確に
   - ❌ `colorful` → ✅ `soft prism colors (Pink, Blue, Red, Green, Yellow)`
4. **エフェクト**: 音楽ジャンルを視覚化
   - Hyperpop → `digital glitch particles`
   - Electro-Rock → `industrial metallic particles`
   - Synth → `holographic patterns`

---

### ステップ6: 完成プロンプトの出力

ステップ5までで最適化したMidjourneyプロンプトを出力します。

**出力形式**:
```
## 🎨 カバーアート Midjourneyプロンプト

[完成プロンプト全文]

**微調整用パラメータ参考**:
- 表情が合わない場合: 表情キーワードを強調（例: `sorrowful`, `joyful`）
- 色が強すぎる場合: `heavily desaturated`, `muted accents`追加
- 構図がずれる場合: 構図キーワードを先頭に移動
- キャラ数が違う場合: `5 girls`, `solo portrait`等を強調
- バリエーション増: `--chaos 10-30`
- スタイライズ調整: `--stylize 50-150`
```

**次のアクション**:
- 出力したプロンプトをMidjourneyで生成（手動実施）
- 生成された画像から最適な1枚を選択・保存

---

### ステップ7: 保存・管理

#### **ファイル命名規則**

```
[アルバム名]_[曲番号]_[曲名]_cover.png

例:
4th_works_04_silent_fire_cover.png
3rd_works_01_countdown_future_cover.png
```

#### **保存先**

```
audio/[アルバム名]/
├── [曲番号]_[曲名]_[バージョン].wav
└── [曲番号]_[曲名]_cover.png
```

**例**:
```
audio/leon-album-4th/
├── 04_静かな炎_final.wav
└── 04_静かな炎_cover.png
```

#### **プロンプト記録**

使用したプロンプトをSunoプロンプトファイルに追記：

```markdown
## 🎨 カバーアート Midjourneyプロンプト

[プロンプト全文]
```

---

## 🎨 キャラクター別ビジュアルガイド

### **ツミカ（カグツチ）**
- **服装**: 白と炭灰色の巫女服、擦り切れた裾
- **髪**: ダークブラウン、長髪
- **目**: 琥珀色、悲しげ
- **ムード**: 儚い、孤独、静かな決意
- **背景**: 火山、炎神、鎖、灰、消えかけの炎
- **カラー**: 寒色系、赤み抑制、かすかな琥珀色

### **ミライ（ミッドガン）**
- **服装**: 近未来的な学生服
- **髪**: 明るい色、ショート〜ミディアム
- **目**: 希望に満ちた
- **ムード**: 希望、決意、テクノロジー
- **背景**: 未来都市、ネオンライト、ホログラム
- **カラー**: ゴールデンイエロー、シアン

### **クルミ（メテオラス）**
- **服装**: フェアリー風、自然素材
- **髪**: パステルグリーン、葉の装飾
- **目**: 輝く、無邪気
- **ムード**: 成長、変身、可愛らしさ
- **背景**: 森、繭、蝶の羽、発光植物
- **カラー**: フォレストグリーン、シアン、虹色

### **リサ（貿易コロニー）**
- **服装**: 宇宙服風、未来的
- **髪**: クールな色、ショート
- **目**: クールで知的
- **ムード**: 自由、冒険、前向き
- **背景**: 宇宙、星、コロニー
- **カラー**: パープル、シルバー、ネオン

### **ミナモ（アクアノーヴァ）**
- **服装**: 海洋風、流れるようなデザイン
- **髪**: 水色、長く流れる
- **目**: 深く包容力のある
- **ムード**: クール、圧倒的存在感
- **背景**: 海、波、水中生物
- **カラー**: アクアブルー、ディープブルー

### **5人ユニット**
- **配置**: 中央にリーダー（ミライ）、両側に4人
- **カラー**: 5色調和（赤、青、緑、黄、紫）
- **ムード**: 絆、希望、調和、エネルギー
- **背景**: 虹、光の柱、デジタル空間

---

## ✅ チェックリスト

制作完了前に以下を確認：

- [ ] 楽曲タイトル・テーマに合致している
- [ ] キャラクター設定（カード根拠）と一致している
- [ ] 歌詞の主要な感情が表現されている
- [ ] カラーパレットが楽曲ジャンルに合っている
- [ ] 既存カバーアートとスタイルが統一されている
- [ ] 解像度が十分（最低1024x1024以上）
- [ ] ファイル名が命名規則に従っている
- [ ] プロンプトが記録されている

---

## 🔄 次のアクション

カバーアート完成後：

1. **README.md更新**: 楽曲一覧にカバーアート情報追記
2. **アルバムフォルダ整理**: 音源とカバーアートをセットで配置
3. **SNS投稿用**: 必要に応じて正方形以外のバージョン作成（16:9等）

---

## 📚 参考資料

- **Midjourneyドキュメント**: https://docs.midjourney.com/
- **Niji v6ガイド**: https://docs.midjourney.com/docs/niji-model
- **カードデータ**: `data/cards.json`
- **世界観分析**: `docs/lore/CNP_TCG_STORY_ANALYSIS.md`
- **既存プロンプト**: `prompts/suno/`配下の各ファイル

---

*このワークフローは、CNP TCG音楽プロジェクトのビジュアルアイデンティティを統一し、効率的にカバーアートを制作するためのガイドラインです。*
