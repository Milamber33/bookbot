def main():
    report = book_report("./books/frankenstein.txt")
    print(report)

def word_count(text):
    return len(text.split())

def char_count(text):
    lower_text = text.lower()
    chars = []
    for i in range(26):
        chars.append({"char":chr(i+97),"count":0})
    for c in lower_text:
        if c.isalpha():
            chars[ord(c)-97]["count"] += 1
    chars.sort(reverse=True, key=sort_count)
    return chars

def sort_count(dict):
    return dict["count"]

def book_report(path):
    with open(path) as f:
        file_contents = f.read()
        w_c = word_count(file_contents)
        chars = char_count(file_contents)
        report = f"--- Begin report of {path} ---\n"
        report += f"{w_c} words found in the document\n\n"
        for c in chars:
            report += f"The '{c['char']}' character was found {c['count']} times\n"
        report += f"--- End report ---"
    return report

main()