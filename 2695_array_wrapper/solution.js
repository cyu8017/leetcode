// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

var ArrayWrapper = function(nums) {
    this.nums = nums;
};

ArrayWrapper.prototype.valueOf = function() {
    let s = 0;
    for (const x of this.nums) s += x;
    return s;
};

ArrayWrapper.prototype.toString = function() {
    return "[" + this.nums.join(",") + "]";
};
