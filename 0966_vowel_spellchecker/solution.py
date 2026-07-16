# LeetCode 0966 - Vowel Spellchecker
# https://leetcode.com/problems/vowel-spellchecker/

class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        vowels = set("aeiou")

        def devowel(w: str) -> str:
            return "".join("*" if c in vowels else c for c in w.lower())

        exact = set(wordlist)
        lower: dict[str, str] = {}
        vowel_map: dict[str, str] = {}
        for w in wordlist:
            low = w.lower()
            lower.setdefault(low, w)
            vowel_map.setdefault(devowel(w), w)

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
            elif q.lower() in lower:
                ans.append(lower[q.lower()])
            elif devowel(q) in vowel_map:
                ans.append(vowel_map[devowel(q)])
            else:
                ans.append("")
        return ans
