// LeetCode 0315 - Count of Smaller Numbers After Self
// https://leetcode.com/problems/count-of-smaller-numbers-after-self/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var countSmaller = function(nums) {
    const sorted = [];
    const result = [];
    for (let index = nums.length - 1; index >= 0; index -= 1) {
        const num = nums[index];
        let left = 0;
        let right = sorted.length;
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (sorted[mid] < num) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        result.push(left);
        sorted.splice(left, 0, num);
    }
    return result.reverse();
};
