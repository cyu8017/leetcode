// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

public class Solution {
    public int LargestPalindrome(int n) {
        if (n == 1) {
            return 9;
        }
        int upper = (int)Math.Pow(10, n) - 1;
        int lower = (int)Math.Pow(10, n - 1);
        for (int first = upper; first >= lower; first--) {
            string firstString = first.ToString();
            long candidate = long.Parse(firstString + new string(firstString.Reverse().ToArray()));
            for (int factor = upper; (long)factor * factor >= candidate; factor--) {
                if (candidate % factor == 0) {
                    int partner = (int)(candidate / factor);
                    if (partner >= lower && partner <= upper) {
                        return (int)(candidate % 1337);
                    }
                }
            }
        }
        return 0;
    }
}
