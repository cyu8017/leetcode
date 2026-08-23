// LeetCode 2716 - Minimize String Length
// https://leetcode.com/problems/minimize-string-length/

var minimizedStringLength = function(s) {
    return new Set(s).size;
};
