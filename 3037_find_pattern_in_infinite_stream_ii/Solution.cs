// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

// Definition for an infinite stream (provided by LeetCode; kept for local builds).
public class InfiniteStream {
    private readonly int[] bits;
    private int i;
    public InfiniteStream(int[] bits) { this.bits = bits; i = 0; }
    public int Next() { return bits[i++]; }
}

public class Solution {
    static int[] GetLPS(int[] pattern) {
        int n = pattern.Length;
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

    public int FindPattern(InfiniteStream stream, int[] pattern) {
        var lps = GetLPS(pattern);
        int i = 0, j = 0, bit = 0;
        bool readNext = false;
        while (true) {
            if (!readNext) {
                bit = stream.Next();
                readNext = true;
            }
            if (bit == pattern[j]) {
                i++;
                readNext = false;
                j++;
                if (j == pattern.Length) return i - j;
            } else if (j > 0) {
                j = lps[j - 1];
            } else {
                i++;
                readNext = false;
            }
        }
    }
}
