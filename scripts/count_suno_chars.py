import sys
import re

def count_suno_style_chars(text):
    """
    SunoのStylesセクション（コードブロック内）の合計文字数を計測する。
    4つの基本セクション（Style/Refs, Vocal, Arrangement, Production）が対象。
    """
    # コードブロックの中身を抽出
    code_match = re.search(r'```(?:\w+)?\n(.*?)\n```', text, re.DOTALL)
    if not code_match:
        # コードブロックがない場合はテキスト全体を対象にする
        content = text.strip()
    else:
        content = code_match.group(1).strip()

    # 改行を含めた純粋な文字数をカウント
    char_count = len(content)
    
    # セクションごとのカウントも表示（デバッグ用）
    lines = content.split('\n')
    print("-" * 30)
    for i, line in enumerate(lines):
        if line.strip():
            print(f"Line {i+1}: {len(line)} chars | {line[:50]}...")
    print("-" * 30)
    
    return char_count

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # ファイルから読み込み
        try:
            with open(sys.argv[1], 'r', encoding='utf-8') as f:
                input_text = f.read()
                # 歌詞部分は除外してStyleセクションだけを特定するために
                # ## 🎵 Sunoプロンプト（完全版） 以下の 【Styles】 セクションを探す
                if "### **【Styles】**" in input_text:
                    style_part = input_text.split("### **【Styles】**")[1].split("---")[0]
                else:
                    style_part = input_text
                
                count = count_suno_style_chars(style_part)
                print(f"TOTAL STYLE CHARACTERS: {count}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: python3 count_suno_chars.py <path_to_prompt_md>")
