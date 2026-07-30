// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] RecoverArray(int n, int[] sums) {
        Array.Sort(sums);
        var list = sums.ToList();
        var ans = new List<int>();
        for (int step = 0; step < n; step++) {
            int d = list[1] - list[0];
            var count = new Dictionary<int, int>();
            foreach (int x in list) count[x] = count.GetValueOrDefault(x) + 1;
            var without = new List<int>();
            var withD = new List<int>();
            foreach (int x in list) {
                if (count.GetValueOrDefault(x) == 0) continue;
                count[x]--;
                count[x + d] = count.GetValueOrDefault(x + d) - 1;
                without.Add(x);
                withD.Add(x + d);
            }
            if (without.Contains(0)) {
                ans.Add(d);
                list = without;
            } else {
                ans.Add(-d);
                list = withD;
            }
        }
        return ans.ToArray();
    }
}