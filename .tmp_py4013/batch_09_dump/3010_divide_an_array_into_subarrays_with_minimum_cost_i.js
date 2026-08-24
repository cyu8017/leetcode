// LeetCode 3010 - Divide an Array Into Subarrays With Minimum Cost I
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

var minimumCost = function(nums) {
    let a = nums[0], b = 100, c = 100;
    for (let i = 1; i < nums.length; i++) {
        const x = nums[i];
        if (x < b) {
            c = b;
            b = x;
        } else if (x < c) {
            c = x;
        }
    }
    return a + b + c;
};
