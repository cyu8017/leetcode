// LeetCode 3452 - Sum of Good Numbers
// https://leetcode.com/problems/sum-of-good-numbers/

var sumOfGoodNumbers = function(nums, k) {
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        let good = true;
        if (i - k >= 0 && x <= nums[i - k]) good = false;
        if (i + k < n && x <= nums[i + k]) good = false;
        if (good) ans += x;
    }
    return ans;
};
