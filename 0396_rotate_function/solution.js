// LeetCode 0396 - Rotate Function
var maxRotateFunction = function (nums) {
    const n = nums.length;
    const total = nums.reduce((sum, value) => sum + value, 0);
    let current = nums.reduce((sum, value, index) => sum + index * value, 0);
    let best = current;

    for (let index = n - 1; index > 0; index -= 1) {
        current += total - n * nums[index];
        best = Math.max(best, current);
    }

    return best;
};

module.exports = { maxRotateFunction };
