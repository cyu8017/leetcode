// LeetCode 3498 - Reverse Degree of a String
// https://leetcode.com/problems/reverse-degree-of-a-string/

var reverseDegree = function(s) {
    let ans = 0;
    for (let i = 0; i < s.length; i++)
        ans += (26 - (s.charCodeAt(i) - 97)) * (i + 1);
    return ans;
};
