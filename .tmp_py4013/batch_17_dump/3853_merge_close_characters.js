// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

var mergeCharacters = function(s, k) {
    const last = new Map();
    let ans = '';
    for (const c of s) {
        const cur = ans.length;
        if (last.has(c) && cur - last.get(c) <= k) continue;
        ans += c;
        last.set(c, cur);
    }
    return ans;
};
