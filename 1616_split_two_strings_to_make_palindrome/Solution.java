// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution {
    public boolean checkPalindromeFormation(String a, String b) {
        return check(a, b) || check(b, a);
    }

    private boolean check(String x, String y) {
        int i = 0, j = x.length() - 1;
        while (i < j && x.charAt(i) == y.charAt(j)) {
            i++;
            j--;
        }
        return isPalindrome(x, i, j) || isPalindrome(y, i, j);
    }

    private boolean isPalindrome(String s, int i, int j) {
        while (i < j) {
            if (s.charAt(i++) != s.charAt(j--)) return false;
        }
        return true;
    }
}
