// LeetCode 3706 - Maximum Distance Between Unequal Words in Array II
// https://leetcode.com/problems/maximum-distance-between-unequal-words-in-array-ii/

export function maxDistance(words: any): any {
    const n = words.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (words[i] !== words[0]) ans = Math.max(ans, i + 1);
        if (words[i] !== words[n - 1]) ans = Math.max(ans, n - i);
    }
    return ans;
}
