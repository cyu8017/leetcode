// LeetCode 3662 - Filter Characters by Frequency
// https://leetcode.com/problems/filter-characters-by-frequency/

export function filterCharacters(s: any, k: any): any {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    let ans = '';
    for (const c of s)
        if (cnt[c.charCodeAt(0) - 97] < k) ans += c;
    return ans;
}
