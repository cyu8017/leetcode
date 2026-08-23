// LeetCode 0728 - Self Dividing Numbers
// https://leetcode.com/problems/self-dividing-numbers/

/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
    const isSelfDividing = (num) => {
        let x = num;
        while (x > 0) {
            const digit = x % 10;
            if (digit === 0 || num % digit !== 0) return false;
            x = Math.floor(x / 10);
        }
        return true;
    };
    const result = [];
    for (let num = left; num <= right; num++) if (isSelfDividing(num)) result.push(num);
    return result;
};
