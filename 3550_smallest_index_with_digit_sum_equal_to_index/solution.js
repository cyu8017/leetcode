// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

var smallestIndex = function(nums) {
    for (let i = 0; i < nums.length; i++) {
        let x = nums[i], s = 0;
        for (; x > 0; x = Math.floor(x / 10)) s += x % 10;
        if (s === i) return i;
    }
    return -1;
};
