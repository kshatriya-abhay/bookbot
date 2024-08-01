def main():
    files = ['books/frankenstein.txt']
    publish_report(files)
        
def publish_report(filenames):
    for file in filenames:
        print(f"--- Begin report of { file } ---")
        with open(file) as f:
            file_contents = f.read()
            words = file_contents.split()
            print(f'{len(words)} words found in the document')
            print()
            character_count(file_contents)

def character_count(text: str):
    lowered_text = text.lower()
    d = {}
    for ch in lowered_text:
        if ch in d.keys():
            d[ch] += 1
        else:
            d[ch] = 1
    charlist = []
    for k in d.keys():
        if not k.isalpha():
            continue
        charlist.append({"name": k, "num": d[k]})
    charlist.sort(reverse=True, key=sort_on)
    for char in charlist:
        print(f"The '{char['name']}' character was found {char['num']} times")

def sort_on(dict):
    return dict["num"]



main()