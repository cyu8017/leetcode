// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

var maxOperations = function(s) {
    let ans = 0, cnt = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') cnt++;
        else if (i > 0 && s[i - 1] === '1') ans += cnt;
    }
    return ans;
};
