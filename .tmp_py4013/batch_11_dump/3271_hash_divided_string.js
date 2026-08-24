// LeetCode 3271 - Hash Divided String
// https://leetcode.com/problems/hash-divided-string/

var stringHash = function(s, k) {
    let out = '';
    for (let i = 0; i < s.length; i += k) {
        let sum = 0;
        for (let j = i; j < i + k; j++) sum += s.charCodeAt(j) - 97;
        out += String.fromCharCode(97 + sum % 26);
    }
    return out;
};
