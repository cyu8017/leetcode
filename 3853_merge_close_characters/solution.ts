// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

export function mergeCharacters(s: any, k: any): any {
    const last = new Map();
    let ans = '';
    for (const c of s) {
        const cur = ans.length;
        if (last.has(c) && cur - last.get(c) <= k) continue;
        ans += c;
        last.set(c, cur);
    }
    return ans;
}
