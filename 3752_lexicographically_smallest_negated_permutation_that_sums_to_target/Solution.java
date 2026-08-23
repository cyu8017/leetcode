// LeetCode 3752 - Lexicographically Smallest Negated Permutation that Sums to Target
// https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] lexicographicallySmallest(int n, long target) {
        long total = 1L * n * (n + 1) / 2;
        if (target < -total || target > total || (total - target) % 2 != 0) return new int[0];
        long remaining = (total - target) / 2;
        boolean[] negative = new boolean[n + 1];
        for (int value = n; value >= 1; value--) {
            if (value <= remaining) {
                negative[value] = true;
                remaining -= value;
            }
        }
        var answer = new ArrayList<Integer>();
        for (int value = n; value >= 1; value--) {
            if (negative[value]) answer.add(-value);
        }
        for (int value = 1; value <= n; value++) {
            if (!negative[value]) answer.add(value);
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
