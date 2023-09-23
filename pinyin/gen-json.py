#!/bin/env python3

# read hanzi.tsv and generate pinyin.json
# columns in hanzi.tsv: rank, character, occurences, cumulative frequency, pinyin, definition
# structure of pinyin.json: {pinyin: [character, ...], ...}
# example: {"a": ["阿", "啊", "呵", "吖", "嗄", "腌", "锕", "阿", "啊", "呵", "吖", "嗄", "腌", "锕"], ...}
# note: the order of characters is decided by rank value in hanzi.tsv

import json

def main():
    with open('hanzi.tsv', 'r') as f:
        lines = f.readlines()

    MAX_RANK = 3000
    hanzi = {}
    for line in lines[:MAX_RANK]:
        line = line.strip()
        if not line or line.startswith('#'):
            continue

        fields = line.split('\t')
        if len(fields) < 5:
            print(f'*** skipping line without pinyin: {line}')
            continue
        # rank, character, occurences, cumulative_frequency, pinyins = fields[:5]
        character, pinyins = fields[1], fields[4]
        for pinyin in pinyins.split('/'):
            pinyin = pinyin.strip('0123456789')
            if pinyin not in hanzi:
                hanzi[pinyin] = ''
            if character not in hanzi[pinyin]:
                hanzi[pinyin] += character

    with open('hanzi.js', 'w') as f:
        hanzi_js = 'var hanzi = ' + json.dumps(hanzi, ensure_ascii=False, indent=3)
        f.write(hanzi_js)

if __name__ == '__main__':
    main()
