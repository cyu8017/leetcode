// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

export function spellchecker(wordlist: string[], queries: string[]): string[] {
    const exact = new Set(wordlist);
    const lowerMap = new Map();
    const vowelMap = new Map();
    const devowel = (w) => w.toLowerCase().replace(/[aeiou]/g, "*");
    for (const w of wordlist) {
        const low = w.toLowerCase();
        if (!lowerMap.has(low)) lowerMap.set(low, w);
        const dv = devowel(w);
        if (!vowelMap.has(dv)) vowelMap.set(dv, w);
    }
    return queries.map((q) => {
        if (exact.has(q)) return q;
        const low = q.toLowerCase();
        if (lowerMap.has(low)) return lowerMap.get(low);
        const dv = devowel(q);
        if (vowelMap.has(dv)) return vowelMap.get(dv);
        return "";
    });
}
