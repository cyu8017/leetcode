// LeetCode 3480 - Maximize Subarrays After Removing One Conflicting Pair
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/

using System.Collections.Generic;

public class Solution {
    public long MaxSubarrays(int n, int[][] conflictingPairs) {
        int m = conflictingPairs.Length;
        long best = 0;
        for (int skip = 0; skip < m; skip++) {
            var banned = new List<(int a, int b)>();
            for (int i = 0; i < m; i++) {
                if (i == skip) continue;
                int a = conflictingPairs[i][0], b = conflictingPairs[i][1];
                if (a > b) { int t = a; a = b; b = t; }
                banned.Add((a, b));
            }
            int[] rightLimit = new int[n + 2];
            for (int i = 0; i < rightLimit.Length; i++) rightLimit[i] = n + 1;
            foreach (var b in banned) {
                if (b.b < rightLimit[b.a]) rightLimit[b.a] = b.b;
            }
            int minRight = n + 1;
            long cnt = 0;
            for (int l = n; l >= 1; l--) {
                if (rightLimit[l] < minRight) minRight = rightLimit[l];
                cnt += minRight - l;
            }
            if (cnt > best) best = cnt;
        }
        return best;
    }
}
