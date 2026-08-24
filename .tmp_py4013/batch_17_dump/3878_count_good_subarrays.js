// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

var countGoodSubarrays = function(nums) {
    const n = nums.length;
    const l = new Array(n).fill(-1);
    const stk = [];
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        while (stk.length > 0 && nums[stk[stk.length - 1]] < x && (nums[stk[stk.length - 1]] | x) === x) {
            stk.pop();
        }
        if (stk.length > 0) l[i] = stk[stk.length - 1];
        stk.push(i);
    }
    const r = new Array(n).fill(n);
    stk.length = 0;
    for (let i = n - 1; i >= 0; i--) {
        while (stk.length > 0 && (nums[stk[stk.length - 1]] | nums[i]) === nums[i]) {
            stk.pop();
        }
        if (stk.length > 0) r[i] = stk[stk.length - 1];
        stk.push(i);
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans += (i - l[i]) * (r[i] - i);
    }
    return ans;
};
