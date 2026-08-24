// LeetCode 2295 - Replace Elements in an Array
// https://leetcode.com/problems/replace-elements-in-an-array/

var arrayChange = function(nums, operations) {
    const pos = new Map();
    for (let i = 0; i < nums.length; i++) pos.set(nums[i], i);
    for (const op of operations) {
        const i = pos.get(op[0]);
        nums[i] = op[1];
        pos.delete(op[0]);
        pos.set(op[1], i);
    }
    return nums;
};
