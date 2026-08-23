// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

/**
 * @param {string} s
 * @return {number}
 */
var minMovesToMakePalindrome = function(s) {
    const b = s.split('');
    let ans = 0;
    while (b.length > 1) {
        let j = b.length - 1;
        while (j > 0 && b[j] !== b[0]) j--;
        if (j === 0) {
            ans += Math.floor(b.length / 2);
            b.shift();
            continue;
        }
        ans += b.length - 1 - j;
        b.splice(j, 1);
        b.shift();
    }
    return ans;
};
