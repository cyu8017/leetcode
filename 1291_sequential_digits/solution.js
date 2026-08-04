// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

/**
 * @param {number} low
 * @param {number} high
 * @return {number[]}
 */
var sequentialDigits = function(low, high) {
    const digits = '123456789';
    const answer = [];
    for (let length = 2; length <= 9; length++) {
        for (let start = 0; start <= 9 - length; start++) {
            const value = Number(digits.slice(start, start + length));
            if (value >= low && value <= high) answer.push(value);
        }
    }
    return answer;
};
