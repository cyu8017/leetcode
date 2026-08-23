// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

class Solution {
    public boolean[] transformStr(String s, String[] strs) {
        int n = s.length();
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + (s.charAt(i) == '1' ? 1 : 0);
        boolean[] result = new boolean[strs.length];
        for (int i = 0; i < strs.length; i++) {
            int left = 0, right = 0;
            boolean ok = true;
            for (int j = 0; j < n; j++) {
                left += (strs[i].charAt(j) == '1' ? 1 : 0);
                int add = (strs[i].charAt(j) != '0' ? 1 : 0);
                right = right + add;
                if (right > prefix[j + 1]) right = prefix[j + 1];
                if (left > right) {
                    ok = false;
                    break;
                }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right;
        }
        return result;
    }
}
