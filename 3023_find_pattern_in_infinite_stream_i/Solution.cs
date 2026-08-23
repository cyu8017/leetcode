// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

// Definition for an infinite stream (provided by LeetCode; kept for local builds).
public class InfiniteStream {
    private readonly int[] bits;
    private int i;
    public InfiniteStream(int[] bits) { this.bits = bits; i = 0; }
    public int Next() { return bits[i++]; }
}

public class Solution {
    public int FindPattern(InfiniteStream stream, int[] pattern) {
        int a = 0, b = 0;
        int m = pattern.Length;
        int half = m >> 1;
        int mask1 = (1 << half) - 1;
        int mask2 = (1 << (m - half)) - 1;
        for (int i = 0; i < half; i++) a |= pattern[i] << (half - 1 - i);
        for (int i = half; i < m; i++) b |= pattern[i] << (m - 1 - i);
        int x = 0, y = 0;
        for (int i = 1; ; i++) {
            int v = stream.Next();
            y = y << 1 | v;
            v = (y >> (m - half)) & 1;
            y &= mask2;
            x = x << 1 | v;
            x &= mask1;
            if (i >= m && a == x && b == y) return i - m;
        }
    }
}
