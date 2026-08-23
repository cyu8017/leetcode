// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

class Solution {
    public int minimumTime(String s) {
        int n = s.length();
        int[] left = new int[n];
        if (s.charAt(0) == '1') left[0] = 1;
        for (int i = 1; i < n; i++) {
            left[i] = left[i - 1];
            if (s.charAt(i) == '1') left[i] = Math.min(i + 1, left[i - 1] + 2);
        }
        int ans = left[n - 1], right = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s.charAt(i) == '1') right = Math.min(n - i, right + 2);
            int leftCost = i > 0 ? left[i - 1] : 0;
            ans = Math.min(ans, leftCost + right);
        }
        return ans;
    }
}
