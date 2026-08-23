// LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
// https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

function smallestProperDivisor(x) {
    for (let d = 2; d * d <= x; d++) if (x % d === 0) return d;
    return x;
}
var minOperations = function(nums) {
    let ops = 0;
    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] <= nums[i + 1]) continue;
        while (nums[i] > nums[i + 1]) {
            const d = smallestProperDivisor(nums[i]);
            if (d === nums[i]) return -1;
            nums[i] = Math.floor(nums[i] / d);
            ops++;
            if (nums[i] > nums[i + 1] && smallestProperDivisor(nums[i]) === nums[i]) return -1;
        }
    }
    return ops;
};
