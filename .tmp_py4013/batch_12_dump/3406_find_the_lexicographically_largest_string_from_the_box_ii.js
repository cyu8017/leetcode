// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

var answerString = function(word, numFriends) {
    if (numFriends === 1) return word;
    const n = word.length;
    const maxLen = n - (numFriends - 1);
    let ans = "";
    for (let i = 0; i < n; i++) {
        let end = i + maxLen;
        if (end > n) end = n;
        const cand = word.substring(i, end);
        if (cand > ans) ans = cand;
    }
    return ans;
};

var solve = answerString;
