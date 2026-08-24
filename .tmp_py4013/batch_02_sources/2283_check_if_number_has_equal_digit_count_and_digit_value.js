// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

var digitCount = function(num) {
    const cnt = new Array(10).fill(0);
    for (const c of num) cnt[c.charCodeAt(0) - 48]++;
    for (let i = 0; i < num.length; i++)
        if (cnt[i] !== num.charCodeAt(i) - 48) return false;
    return true;
};
