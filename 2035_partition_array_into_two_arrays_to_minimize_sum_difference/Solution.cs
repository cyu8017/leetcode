// LeetCode 2035 - Partition Array Into Two Arrays to Minimize Sum Difference
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinimumDifference(int[] nums) {
        int n = nums.Length / 2;
        int total = nums.Sum();
        List<int>[] SumsByCount(int[] arr) {
            int m = arr.Length;
            var res = new List<int>[m + 1];
            for (int i = 0; i <= m; i++) res[i] = new List<int>();
            for (int mask = 0; mask < (1 << m); mask++) {
                int sum = 0, c = 0;
                for (int i = 0; i < m; i++) if ((mask & (1 << i)) != 0) { sum += arr[i]; c++; }
                res[c].Add(sum);
            }
            foreach (var v in res) v.Sort();
            return res;
        }
        int[] left = nums.Take(n).ToArray();
        int[] right = nums.Skip(n).ToArray();
        var L = SumsByCount(left);
        var R = SumsByCount(right);
        int ans = int.MaxValue;
        for (int k = 0; k <= n; k++) {
            foreach (int s1 in L[k]) {
                int need = total / 2 - s1;
                var arr = R[n - k];
                int idx = arr.BinarySearch(need);
                if (idx < 0) idx = ~idx;
                foreach (int j in new[] { idx - 1, idx }) {
                    if (j >= 0 && j < arr.Count) {
                        int s2 = arr[j];
                        ans = Math.Min(ans, Math.Abs(total - 2 * (s1 + s2)));
                    }
                }
            }
        }
        return ans;
    }
}
