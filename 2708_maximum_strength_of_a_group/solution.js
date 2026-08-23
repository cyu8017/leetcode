// LeetCode 2708 - Maximum Strength of a Group
// https://leetcode.com/problems/maximum-strength-of-a-group/

var maxStrength = function(nums) {
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    if (n === 1) return nums[0];
    let prod = 1, used = false, i = 0;
    while (i + 1 < n && nums[i] < 0 && nums[i + 1] < 0) {
        prod *= nums[i] * nums[i + 1];
        used = true;
        i += 2;
    }
    const negLeft = i < n && nums[i] < 0;
    for (; i < n; i++) {
        if (nums[i] > 0) {
            prod *= nums[i];
            used = true;
        }
    }
    if (!used) {
        if (negLeft) {
            for (const x of nums) if (x === 0) return 0;
            return nums[n - 1];
        }
        return 0;
    }
    return prod;
};
