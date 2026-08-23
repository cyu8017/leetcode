// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        Set<Integer> s = new HashSet<>();
        for (int x0 : arr1) {
            for (int x = x0; x > 0; x /= 10) s.add(x);
        }
        int mx = 0;
        for (int x0 : arr2) {
            for (int x = x0; x > 0; x /= 10) {
                if (s.contains(x)) {
                    mx = Math.max(mx, x);
                    break;
                }
            }
        }
        return mx > 0 ? Integer.toString(mx).length() : 0;
    }
}
