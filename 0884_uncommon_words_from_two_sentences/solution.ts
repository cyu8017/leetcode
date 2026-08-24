// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

export function uncommonFromSentences(s1: string, s2: string): string[] {
    const count = new Map();
    const add = (s) => {
        for (const w of s.split(" ")) {
            if (!w) continue;
            count.set(w, (count.get(w) || 0) + 1);
        }
    };
    add(s1);
    add(s2);
    const ans = [];
    for (const [k, v] of count) if (v === 1) ans.push(k);
    return ans;
}
