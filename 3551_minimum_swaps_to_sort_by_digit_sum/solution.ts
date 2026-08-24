// LeetCode 3551 - Minimum Swaps to Sort by Digit Sum
// https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/

function f3551(x: any): any {
    let s = 0;
    while (x !== 0) { s += x % 10; x = Math.floor(x / 10); }
    return s;
}export function minSwaps(nums: any): any {
    const n = nums.length;
    const arr = Array.from({length: n}, (_, i) => [f3551(nums[i]), nums[i]]);
    arr.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : a[1] - b[1]);
    const d = new Map();
    for (let i = 0; i < n; i++) d.set(arr[i][1], i);
    const vis = new Array(n).fill(false);
    let ans = n;
    for (let i = 0; i < n; i++) {
        if (!vis[i]) {
            ans--;
            let j = i;
            while (!vis[j]) {
                vis[j] = true;
                j = d.get(nums[j]);
            }
        }
    }
    return ans;
}
