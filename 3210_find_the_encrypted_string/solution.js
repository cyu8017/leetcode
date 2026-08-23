// LeetCode 3210 - Find the Encrypted String
// https://leetcode.com/problems/find-the-encrypted-string/

var getEncryptedString = function(s, k) {
    const n = s.length;
    let out = '';
    for (let i = 0; i < n; i++) out += s[(i + k) % n];
    return out;
};
