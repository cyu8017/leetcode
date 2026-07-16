// LeetCode 0009 - Palindrome Number
// https://leetcode.com/problems/palindrome-number/

export function isPalindrome(x: number): boolean {
    if (x < 0 || (x !== 0 && x % 10 === 0)) {
        return false;
    }

    let reversedHalf = 0;
    while (x > reversedHalf) {
        reversedHalf = reversedHalf * 10 + x % 10;
        x = Math.floor(x / 10);
    }

    return x === reversedHalf || x === Math.floor(reversedHalf / 10);
}
