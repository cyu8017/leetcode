// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution {
    public String getSmallestString(String s, int k) {
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            char c1 = arr[i];
            for (char c2 = 'a'; c2 < c1; c2++) {
                int d = Math.min(c1 - c2, 26 - (c1 - c2));
                if (d <= k) {
                    arr[i] = c2;
                    k -= d;
                    break;
                }
            }
        }
        return new String(arr);
    }
}
