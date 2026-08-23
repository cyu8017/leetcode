// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

class Solution {
    convertToBase7(num) {
        if (num === 0) return "0";
        const negative = num < 0;
        num = Math.abs(num);
        const digits = [];
        while (num) {
            digits.push(String(num % 7));
            num = Math.floor(num / 7);
        }
        const result = digits.reverse().join("");
        return negative ? `-${result}` : result;
    }
}

module.exports = { Solution };
