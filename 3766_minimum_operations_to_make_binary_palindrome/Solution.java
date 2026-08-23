// LeetCode 3766 - Minimum Operations To Make Binary Palindrome
// https://leetcode.com/problems/minimum_operations_to_make_binary_palindrome/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final List<Integer> PALS = new ArrayList<>();
    static {
        int N = 1 << 14;
        for (int i = 0; i < N; i++) {
            StringBuilder sb = new StringBuilder();
            int x = i;
            if (x == 0) sb.append('0');
            else {
                while (x > 0) {
                    sb.append((char) ('0' + (x & 1)));
                    x >>= 1;
                }
                sb.reverse();
            }
            if (isPalindrome(sb)) PALS.add(i);
        }
    }

    private static boolean isPalindrome(StringBuilder s) {
        int m = s.length();
        for (int i = 0; i < m / 2; i++) if (s.charAt(i) != s.charAt(m - 1 - i)) return false;
        return true;
    }

    public int[] minOperations(int[] nums) {
        int[] ans = new int[nums.length];
        for (int k = 0; k < nums.length; k++) {
            int x = nums[k];
            int it = lowerBound(x);
            int t = Integer.MAX_VALUE;
            if (it < PALS.size()) t = PALS.get(it) - x;
            if (it > 0) t = Math.min(t, x - PALS.get(it - 1));
            ans[k] = t;
        }
        return ans;
    }

    private int lowerBound(int x) {
        int lo = 0, hi = PALS.size();
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (PALS.get(mid) < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
