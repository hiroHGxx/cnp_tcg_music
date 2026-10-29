import re

with open("prompts/suno/5th_works/03_CNP_5TH_TSUMIKA_VS_KAGEROU_claude_SUNO_PROMPT.md", "r", encoding="utf-8") as f:
    text = f.read()

# 正規表現で【Styles】セクション内の ``` ～ ``` の中身を抽出
match = re.search(r'### \*\*【Styles】\*\*\n+```(?:\w*\n)?(.*?)```', text, re.DOTALL)
if match:
    styles_content = match.group(1).strip()
    # "\n" も1文字としてカウント
    count = len(styles_content)
    print(f"Count: {count}")
else:
    print("Styles section not found.")
