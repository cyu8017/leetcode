// LeetCode 1788 - Maximize the Beauty of the Garden
// https://leetcode.com/problems/maximize-the-beauty-of-the-garden/

public class Solution {
    public int MaximumBeauty(int[] flowers) {
        var first = new Dictionary<int, int>();
        var prefix = new long[flowers.Length + 1];
        for (int i = 0; i < flowers.Length; i++) {
            prefix[i + 1] = prefix[i] + Math.Max(flowers[i], 0);
        }
        long best = long.MinValue;
        for (int i = 0; i < flowers.Length; i++) {
            int value = flowers[i];
            if (first.TryGetValue(value, out int left)) {
                long between = prefix[i] - prefix[left + 1];
                best = Math.Max(best, (long)flowers[left] + flowers[i] + between);
            } else {
                first[value] = i;
            }
        }
        return (int)best;
    }
}
