// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

function countCharacters(words: string[], chars: string): number {
    const avail = new Map();
    for (const c of chars) avail.set(c, (avail.get(c) || 0) + 1);
    let ans = 0;
    for (const word of words) {
        const need = new Map();
        let ok = true;
        for (const c of word) {
            need.set(c, (need.get(c) || 0) + 1);
            if ((avail.get(c) || 0) < need.get(c)) { ok = false; break; }
        }
        if (ok) ans += word.length;
    }
    return ans;
}
