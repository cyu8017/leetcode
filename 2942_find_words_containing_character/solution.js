// LeetCode 2942 - Find Words Containing Character
// https://leetcode.com/problems/find-words-containing-character/

var findWordsContaining = function(words, x) {
    const ans = [];
    for (let i = 0; i < words.length; i++) {
        if (words[i].indexOf(x) >= 0) ans.push(i);
    }
    return ans;
};
