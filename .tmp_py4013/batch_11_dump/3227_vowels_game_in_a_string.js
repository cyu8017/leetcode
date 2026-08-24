// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

var doesAliceWin = function(s) {
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c === 'a' || c === 'e' || c === 'i' || c === 'o' || c === 'u') return true;
    }
    return false;
};
