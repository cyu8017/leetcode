// LeetCode 1663 - Smallest String With A Given Numeric Value
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

import java.util.Arrays;

class Solution {
    public String getSmallestString(int n, int k) {
        char[] ans = new char[n];
        Arrays.fill(ans, 'a');
        k -= n;
        for (int i = n - 1; i >= 0 && k > 0; i--) {
            int d = Math.min(25, k);
            ans[i] = (char) ('a' + d);
            k -= d;
        }
        return new String(ans);
    }
}
