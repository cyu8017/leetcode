// LeetCode 3998 - Transform Binary String Using Subsequence Sort
// https://leetcode.com/problems/transform-binary-string-using-subsequence-sort/

public class Solution {
    public bool[] TransformStr(string s, string[] strs) {
        int n = s.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + (s[i] == '1' ? 1 : 0);
        bool[] result = new bool[strs.Length];
        for (int i = 0; i < strs.Length; i++) {
            int left = 0, right = 0;
            bool ok = true;
            for (int j = 0; j < n; j++) {
                left += (strs[i][j] == '1' ? 1 : 0);
                int add = (strs[i][j] != '0' ? 1 : 0);
                right = right + add;
                if (right > prefix[j + 1]) right = prefix[j + 1];
                if (left > right) { ok = false; break; }
            }
            result[i] = ok && left <= prefix[n] && prefix[n] <= right;
        }
        return result;
    }
}
