// LeetCode 3813 - Vowel Consonant Score
// https://leetcode.com/problems/vowel-consonant-score/

var vowelConsonantScore = function(s) {
    let v = 0, c = 0;
    for (const ch of s) {
        if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            c++;
            if (ch === 'a' || ch === 'e' || ch === 'i' || ch === 'o' || ch === 'u') v++;
        }
    }
    c -= v;
    if (c === 0) return 0;
    return Math.floor(v / c);
};
