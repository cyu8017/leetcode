// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

export function isAlienSorted(words: string[], order: string): boolean {
    const rank = new Array(26);
    for (let i = 0; i < 26; i++) rank[order.charCodeAt(i) - 97] = i;
    const lessEq = (a, b) => {
        const n = Math.min(a.length, b.length);
        for (let i = 0; i < n; i++) {
            const ra = rank[a.charCodeAt(i) - 97], rb = rank[b.charCodeAt(i) - 97];
            if (ra !== rb) return ra < rb;
        }
        return a.length <= b.length;
    };
    for (let i = 0; i + 1 < words.length; i++)
        if (!lessEq(words[i], words[i + 1])) return false;
    return true;
}
