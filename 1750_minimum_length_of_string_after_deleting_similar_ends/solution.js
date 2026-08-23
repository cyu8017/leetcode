// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

/**
 * @param {string} s
 * @return {number}
 */
var minimumLength = function(s) {
    let left = 0;
    let right = s.length - 1;
    while (left < right && s[left] === s[right]) {
        const ch = s[left];
        while (left <= right && s[left] === ch) {
            left++;
        }
        while (left <= right && s[right] === ch) {
            right--;
        }
    }
    return right - left + 1;
};
