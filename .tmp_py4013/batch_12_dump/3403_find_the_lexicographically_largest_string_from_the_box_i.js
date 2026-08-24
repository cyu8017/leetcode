// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

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
