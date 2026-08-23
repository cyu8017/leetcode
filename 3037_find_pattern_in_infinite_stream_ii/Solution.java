// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

class InfiniteStream {
    private final int[] bits;
    private int i;
    public InfiniteStream(int[] bits) { this.bits = bits; i = 0; }
    public int next() { return bits[i++]; }
}

class Solution {
    private static int[] getLPS(int[] pattern) {
        int n = pattern.length;
        int[] lps = new int[n];
        int j = 0;
        for (int i = 1; i < n; i++) {
            while (j > 0 && pattern[j] != pattern[i]) j = lps[j - 1];
            if (pattern[i] == pattern[j]) {
                j++;
                lps[i] = j;
            }
        }
        return lps;
    }

    public int findPattern(InfiniteStream stream, int[] pattern) {
        int[] lps = getLPS(pattern);
        int i = 0, j = 0, bit = 0;
        boolean readNext = false;
        while (true) {
            if (!readNext) {
                bit = stream.next();
                readNext = true;
            }
            if (bit == pattern[j]) {
                i++;
                readNext = false;
                j++;
                if (j == pattern.length) return i - j;
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
                readNext = false;
            }
        }
    }
}
