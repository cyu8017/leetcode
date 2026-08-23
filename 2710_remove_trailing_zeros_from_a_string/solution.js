// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

var removeTrailingZeros = function(num) {
    let end = num.length;
    while (end > 0 && num[end - 1] === "0") end--;
    return num.slice(0, end);
};
