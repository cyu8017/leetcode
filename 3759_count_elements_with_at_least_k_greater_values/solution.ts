// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

export function countElements(nums: any, k: any): any {
    const n = nums.length;
    if (k === 0) return n;
    const a = nums.slice().sort((x, y) => x - y);
    let ans = 0;
    for (let i = 0; i < n - k; i++) {
        if (a[n - k] > a[i]) ans++;
    }
    return ans;
}
