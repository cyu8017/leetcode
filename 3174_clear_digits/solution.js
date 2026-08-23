// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

var clearDigits = function(s) {
    const stk = [];
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c >= '0' && c <= '9') stk.pop();
        else stk.push(c);
    }
    return stk.join('');
};
