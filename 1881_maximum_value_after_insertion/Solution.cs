// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

public class Solution {
    public string MaxValue(string n, int x) {
        bool neg = n[0] == '-';
        int start = neg ? 1 : 0;
        for (int i = start; i < n.Length; i++) {
            int d = n[i] - '0';
            if (neg) {
                if (d > x) {
                    return n.Substring(0, i) + x + n.Substring(i);
                }
            } else if (d < x) {
                return n.Substring(0, i) + x + n.Substring(i);
            }
        }
        return n + x;
    }
}
