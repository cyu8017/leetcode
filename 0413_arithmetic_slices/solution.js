// LeetCode 0413 - Arithmetic Slices
var numberOfArithmeticSlices = function (nums) {
    if (nums.length < 3) return 0;
    let total = 0;
    let current = 0;
    for (let index = 2; index < nums.length; index += 1) {
        if (nums[index] - nums[index - 1] === nums[index - 1] - nums[index - 2]) {
            current += 1;
            total += current;
        } else current = 0;
    }
    return total;
};

module.exports = { numberOfArithmeticSlices };
