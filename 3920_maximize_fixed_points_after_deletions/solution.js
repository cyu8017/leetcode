// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

var maxFixedPoints = function(nums) {
    const tails = [];
    for (let i = 0; i < nums.length; i++) {
        if (i < nums[i]) continue;
        const d = i - nums[i];
        let lo = 0, hi = tails.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (tails[mid] < d) lo = mid + 1;
            else hi = mid;
        }
        if (lo === tails.length) tails.push(d);
        else tails[lo] = d;
    }
    return tails.length;
};
