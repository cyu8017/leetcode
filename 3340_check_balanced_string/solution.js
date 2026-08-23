// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

var isBalanced = function(num) {
    let even = 0, odd = 0;
    for (let i = 0; i < num.length; i++) {
        if (i % 2 === 0) even += num.charCodeAt(i) - 48;
        else odd += num.charCodeAt(i) - 48;
    }
    return even === odd;
};
