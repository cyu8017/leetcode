// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

var makeSmallestPalindrome = function(s) {
    const arr = s.split("");
    const n = arr.length;
    for (let i = 0; i < n / 2; i++) {
        const c = arr[i] < arr[n - 1 - i] ? arr[i] : arr[n - 1 - i];
        arr[i] = arr[n - 1 - i] = c;
    }
    return arr.join("");
};
