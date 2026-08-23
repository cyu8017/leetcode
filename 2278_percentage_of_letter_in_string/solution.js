// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

var percentageLetter = function(s, letter) {
    let cnt = 0;
    for (const c of s) if (c === letter) cnt++;
    return Math.floor(cnt * 100 / s.length);
};
