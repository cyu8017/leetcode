// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/

public class Solution {
    public bool IsFascinating(int n) {
        string s = n.ToString() + (2 * n).ToString() + (3 * n).ToString();
        if (s.Length != 9) return false;
        int[] cnt = new int[10];
        foreach (char c in s) cnt[c - '0']++;
        if (cnt[0] != 0) return false;
        for (int i = 1; i <= 9; i++) if (cnt[i] != 1) return false;
        return true;
    }
}
