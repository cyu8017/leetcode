// LeetCode 3790 - Smallest All Ones Multiple
// https://leetcode.com/problems/smallest-all-ones-multiple/

export function minAllOneMultiple(k: any): any {
    if ((k & 1) === 0) return -1;
    let x = 1 % k;
    let ans = 1;
    for (let i = 0; i < k; i++) {
        x = (x * 10 + 1) % k;
        ans++;
        if (x === 0) return ans;
    }
    return -1;
}
