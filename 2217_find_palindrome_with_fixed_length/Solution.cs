// LeetCode 2217 - Find Palindrome With Fixed Length
// https://leetcode.com/problems/find-palindrome-with-fixed-length/

public class Solution {
    public long[] KthPalindrome(int[] queries, int intLength) {
        int half = (intLength + 1) / 2;
        int start = 1;
        for (int i = 1; i < half; i++) start *= 10;
        int total = start * 9;
        long[] ans = new long[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int q = queries[i];
            if (q > total) { ans[i] = -1; continue; }
            int left = start + q - 1;
            long pal = left;
            int x = left;
            if (intLength % 2 != 0) x /= 10;
            while (x > 0) { pal = pal * 10 + x % 10; x /= 10; }
            ans[i] = pal;
        }
        return ans;
    }
}
