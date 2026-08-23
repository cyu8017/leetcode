// LeetCode 3795 - Minimum Subarray Length With Distinct Sum At Least K
// https://leetcode.com/problems/minimum_subarray_length_with_distinct_sum_at_least_k/

var minLength = function(nums, k) {
    const n = nums.length;
    let ans = n + 1, l = 0;
    const cnt = new Map();
    let s = 0;
    for (let r = 0; r < n; r++) {
        const c = (cnt.get(nums[r]) || 0) + 1;
        cnt.set(nums[r], c);
        if (c === 1) s += nums[r];
        while (s >= k) {
            if (r - l + 1 < ans) ans = r - l + 1;
            const left = nums[l];
            const nc = cnt.get(left) - 1;
            if (nc === 0) {
                cnt.delete(left);
                s -= left;
            } else cnt.set(left, nc);
            l++;
        }
    }
    return ans > n ? -1 : ans;
};
