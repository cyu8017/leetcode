// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

/**
 * @param {string} expression
 * @return {number[]}
 */
var diffWaysToCompute = function(expression) {
    if (/^\d+$/.test(expression)) {
        return [parseInt(expression, 10)];
    }
    const result = [];
    for (let index = 0; index < expression.length; index++) {
        const char = expression[index];
        if (char !== '+' && char !== '-' && char !== '*') {
            continue;
        }
        const left = diffWaysToCompute(expression.slice(0, index));
        const right = diffWaysToCompute(expression.slice(index + 1));
        for (const leftValue of left) {
            for (const rightValue of right) {
                if (char === '+') {
                    result.push(leftValue + rightValue);
                } else if (char === '-') {
                    result.push(leftValue - rightValue);
                } else {
                    result.push(leftValue * rightValue);
                }
            }
        }
    }
    return result;
};
