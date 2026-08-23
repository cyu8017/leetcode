// LeetCode 3892 - Minimum Operations to Achieve At Least K Peaks
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/

using System;

public class Solution {
    public long MinOperations(int[] nums, int k) {
        int n = nums.Length;
        if (k == 0) return 0;
        if (k > n / 2) return -1;
        var cost = new long[n];
        for (int i = 0; i < n; i++) {
            int left = nums[(i + n - 1) % n], right = nums[(i + 1) % n];
            int need = Math.Max(left, right);
            if (need >= nums[i]) cost[i] = (long)need - nums[i] + 1;
        }
        const long inf = 1L << 60;

        long Line(int left, int right, int choose) {
            if (choose == 0) return 0;
            if (left > right || choose > (right - left + 2) / 2) return inf;
            var prev2 = new long[choose + 1];
            var prev1 = new long[choose + 1];
            Array.Fill(prev2, inf); Array.Fill(prev1, inf);
            prev2[0] = prev1[0] = 0;
            for (int i = left; i <= right; i++) {
                var current = (long[])prev1.Clone();
                for (int j = 1; j <= choose; j++) {
                    if (prev2[j - 1] != inf && prev2[j - 1] + cost[i] < current[j]) {
                        current[j] = prev2[j - 1] + cost[i];
                    }
                }
                prev2 = prev1;
                prev1 = current;
            }
            return prev1[choose];
        }

        long answer = Line(1, n - 1, k);
        long withFirst = Line(2, n - 2, k - 1);
        if (withFirst != inf) {
            withFirst += cost[0];
            answer = Math.Min(answer, withFirst);
        }
        if (answer == inf) return -1;
        return answer;
    }
}
