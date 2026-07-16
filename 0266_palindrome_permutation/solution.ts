// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

function canPermutePalindrome(s: string): boolean {
    const counts = new Array(26).fill(0);
    for (const char of s) {
        counts[char.charCodeAt(0) - 97]++;
    }
    let odd = 0;
    for (const count of counts) {
        if (count % 2) {
            odd++;
        }
    }
    return odd <= 1;
}
