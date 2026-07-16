// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

/**
 * @param {number[]} heights
 * @return {number}
 */
var largestRectangleArea = function(heights) {
    const stack = [];
    let maxArea = 0;
    const extended = heights.concat([0]);

    for (let i = 0; i < extended.length; i++) {
        const height = extended[i];
        while (stack.length > 0 && extended[stack[stack.length - 1]] > height) {
            const h = extended[stack.pop()];
            const width = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
            maxArea = Math.max(maxArea, h * width);
        }
        stack.push(i);
    }

    return maxArea;
};
