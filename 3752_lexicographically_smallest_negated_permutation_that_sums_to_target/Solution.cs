// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

using System.Collections.Generic;

public class Solution {
    public int[] LexicographicallySmallest(int n, long target) {
        long total = 1L * n * (n + 1) / 2;
        if (target < -total || target > total || (total - target) % 2 != 0) return new int[0];
        long remaining = (total - target) / 2;
        bool[] negative = new bool[n + 1];
        for (int value = n; value >= 1; value--) {
            if (value <= remaining) {
                negative[value] = true;
                remaining -= value;
            }
        }
        var answer = new List<int>();
        for (int value = n; value >= 1; value--) {
            if (negative[value]) answer.Add(-value);
        }
        for (int value = 1; value <= n; value++) {
            if (!negative[value]) answer.Add(value);
        }
        return answer.ToArray();
    }
}
