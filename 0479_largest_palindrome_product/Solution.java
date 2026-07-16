// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

class Solution {
    public int largestPalindrome(int n) {
        if (n == 1) {
            return 9;
        }
        int upper = (int) Math.pow(10, n) - 1;
        int lower = (int) Math.pow(10, n - 1);
        for (int first = upper; first >= lower; first--) {
            String firstString = Integer.toString(first);
            StringBuilder reversed = new StringBuilder(firstString).reverse();
            long candidate = Long.parseLong(firstString + reversed);
            for (int factor = upper; (long) factor * factor >= candidate; factor--) {
                if (candidate % factor == 0) {
                    int partner = (int) (candidate / factor);
                    if (partner >= lower && partner <= upper) {
                        return (int) (candidate % 1337);
                    }
                }
            }
        }
        return 0;
    }
}
