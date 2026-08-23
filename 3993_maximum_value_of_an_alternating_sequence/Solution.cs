// LeetCode 3993 - Maximum Value of an Alternating Sequence
// https://leetcode.com/problems/maximum-value-of-an-alternating-sequence/

public class Solution {
    public long MaximumValue(int n, int s, int m) {
        if (n == 1) return s;
        return (long)s + (long)(n / 2) * (m - 1) + 1;
    }
}
