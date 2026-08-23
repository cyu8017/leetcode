// LeetCode 2560 - House Robber IV
// https://leetcode.com/problems/house-robber-iv/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minCapability = function(nums, k) {
    let lo = Math.min(...nums), hi = Math.max(...nums);
    const ok = (cap) => {
        let cnt = 0;
        for (let i = 0; i < nums.length;) {
            if (nums[i] <= cap) {
                cnt++;
                i += 2;
            } else i++;
        }
        return cnt >= k;
    };
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
