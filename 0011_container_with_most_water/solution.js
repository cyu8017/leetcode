// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let best = 0;

    while (left < right) {
        const width = right - left;
        best = Math.max(best, Math.min(height[left], height[right]) * width);
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return best;
};
