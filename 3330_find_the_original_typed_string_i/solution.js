// LeetCode 3330 - Find the Original Typed String I
// https://leetcode.com/problems/find-the-original-typed-string-i/

var possibleStringCount = function(word) {
    let ans = 1;
    for (let i = 1; i < word.length; i++) {
        if (word[i] === word[i - 1]) ans++;
    }
    return ans;
};
