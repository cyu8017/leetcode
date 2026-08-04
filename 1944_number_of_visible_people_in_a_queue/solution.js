// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

/**
 * @param {number[]} heights
 * @return {number[]}
 */
var canSeePersonsCount = function(heights) {
    const n = heights.length;
    const ans = new Array(n).fill(0);
    const stack = [];
    for (let i = n - 1; i >= 0; i--) {
        let count = 0;
        while (stack.length && heights[i] > stack[stack.length - 1]) {
            stack.pop();
            count++;
        }
        if (stack.length) count++;
        ans[i] = count;
        stack.push(heights[i]);
    }
    return ans;
};
