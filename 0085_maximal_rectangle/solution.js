// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
    if (!matrix || matrix.length === 0) {
        return 0;
    }

    const cols = matrix[0].length;
    const heights = new Array(cols).fill(0);
    let maxArea = 0;

    for (let r = 0; r < matrix.length; r++) {
        for (let j = 0; j < cols; j++) {
            heights[j] = matrix[r][j] === '1' ? heights[j] + 1 : 0;
        }
        maxArea = Math.max(maxArea, largestHistogram(heights));
    }

    return maxArea;
};

/**
 * @param {number[]} heights
 * @return {number}
 */
function largestHistogram(heights) {
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
}
