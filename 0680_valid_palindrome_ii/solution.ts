// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

export function validPalindrome(s: string): boolean {
    const isPalindrome = (left, right) => {
        while (left < right) {
            if (s[left] !== s[right]) return false;
            left++;
            right--;
        }
        return true;
    };
    let left = 0, right = s.length - 1;
    while (left < right) {
        if (s[left] !== s[right]) {
            return isPalindrome(left + 1, right) || isPalindrome(left, right - 1);
        }
        left++;
        right--;
    }
    return true;
}
