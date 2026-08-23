// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

var hasSameDigits = function(s) {
    let b = s.split("");
    while (b.length > 2) {
        const nb = new Array(b.length - 1);
        for (let i = 0; i + 1 < b.length; i++) {
            nb[i] = String((b[i].charCodeAt(0) - 48 + b[i + 1].charCodeAt(0) - 48) % 10);
        }
        b = nb;
    }
    return b[0] === b[1];
};
