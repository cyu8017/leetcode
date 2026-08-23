// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

/**
 * @param {number[]} nums
 * @param {number} p
 * @return {number}
 */
var minimizeMax = function(nums, p) {
    nums.sort((a, b) => a - b);
    let lo = 0, hi = nums[nums.length - 1] - nums[0];
    const ok = (d) => {
        let cnt = 0;
        for (let i = 0; i + 1 < nums.length;) {
            if (nums[i + 1] - nums[i] <= d) {
                cnt++;
                i += 2;
            } else i++;
        }
        return cnt >= p;
    };
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
};
