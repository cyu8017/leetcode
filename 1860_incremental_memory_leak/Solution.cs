// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

public class Solution {
    public int[] MemLeak(int memory1, int memory2) {
        int m1 = memory1;
        int m2 = memory2;
        int second = 1;
        while (m1 >= second || m2 >= second) {
            if (m1 >= m2) {
                m1 -= second;
            } else {
                m2 -= second;
            }
            second++;
        }
        return new[] { second, m1, m2 };
    }
}
