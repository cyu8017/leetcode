// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    let num = [...s].map((c) => String(c.charCodeAt(0) - 96)).join("");
    for (let i = 0; i < k; i++) {
        let sum = 0;
        for (const d of num) sum += d.charCodeAt(0) - 48;
        num = String(sum);
    }
    return Number(num);
};
