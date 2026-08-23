// LeetCode 3723 - Maximize Sum Of Squares Of Digits
// https://leetcode.com/problems/maximize_sum_of_squares_of_digits/

var maxSumOfSquares = function(num, sum) {
    if (num * 9 < sum) return "";
    const k = Math.floor(sum / 9), s = sum % 9;
    let ans = '';
    for (let i = 0; i < k; i++) ans += '9';
    if (s > 0) ans += String.fromCharCode(48 + s);
    while (ans.length < num) ans += '0';
    return ans;
};
