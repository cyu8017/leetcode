// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

class Solution {
    public String maxValue(String n, int x) {
        boolean neg = n.charAt(0) == '-';
        int start = neg ? 1 : 0;
        for (int i = start; i < n.length(); i++) {
            int d = n.charAt(i) - '0';
            if (neg) {
                if (d > x) {
                    return n.substring(0, i) + x + n.substring(i);
                }
            } else if (d < x) {
                return n.substring(0, i) + x + n.substring(i);
            }
        }
        return n + x;
    }
}
