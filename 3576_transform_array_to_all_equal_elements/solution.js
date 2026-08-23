// LeetCode 3576 - Transform Array to All Equal Elements
// https://leetcode.com/problems/transform-array-to-all-equal-elements/

function check3576(nums, target, kk) {
    let cnt = 0, sign = 1;
    for (let i = 0; i < nums.length - 1; i++) {
        const x = nums[i] * sign;
        if (x === target) sign = 1;
        else {
            sign = -1;
            cnt++;
        }
    }
    return cnt <= kk && nums[nums.length - 1] * sign === target;
}
var canMakeEqual = function(nums, k) {
    return check3576(nums, nums[0], k) || check3576(nums, -nums[0], k);
};
