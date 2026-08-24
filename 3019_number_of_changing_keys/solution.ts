// LeetCode 3019 - Number of Changing Keys
// https://leetcode.com/problems/number-of-changing-keys/

export function countKeyChanges(s: any): any {
    s = s.toLowerCase();
    let ans = 0;
    for (let i = 1; i < s.length; i++)
        if (s[i] !== s[i - 1]) ans++;
    return ans;
}
