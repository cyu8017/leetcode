// LeetCode 3270 - Find the Key of the Numbers
// https://leetcode.com/problems/find-the-key-of-the-numbers/

var generateKey = function(num1, num2, num3) {
    let ans = 0, mul = 1;
    for (let t = 0; t < 4; t++) {
        const d = Math.min(num1 % 10, num2 % 10, num3 % 10);
        ans += d * mul;
        mul *= 10;
        num1 = Math.floor(num1 / 10); num2 = Math.floor(num2 / 10); num3 = Math.floor(num3 / 10);
    }
    return ans;
};
