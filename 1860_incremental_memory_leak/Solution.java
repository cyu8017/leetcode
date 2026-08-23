// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

class Solution {
    public int[] memLeak(int memory1, int memory2) {
        int second = 1;

        while (memory1 >= second || memory2 >= second) {
            if (memory1 >= memory2) {
                memory1 -= second;
            } else {
                memory2 -= second;
            }
            second++;
        }

        return new int[] { second, memory1, memory2 };
    }
}
