// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

export function minOperations(s: any): any {
    let ans = 0;
    for (const c of s) {
        if (c !== 'a') ans = Math.max(ans, 26 - (c.charCodeAt(0) - 97));
    }
    return ans;
}
