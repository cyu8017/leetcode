// LeetCode 1342 - Number Of Steps To Reduce A Number To Zero
// https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps = function(num) {
    let steps = 0;
    while (num) {
        num = num % 2 === 0 ? num / 2 : num - 1;
        steps++;
    }
    return steps;
};
