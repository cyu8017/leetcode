// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool CanReorderDoubled(int[] arr) {
        var count = new SortedDictionary<int, int>();
        foreach (int x in arr) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        var keys = count.Keys.OrderBy(x => Math.Abs(x)).ToList();
        foreach (int x in keys) {
            if (count[x] == 0) continue;
            int need = count[x];
            if (!count.ContainsKey(2 * x) || count[2 * x] < need) return false;
            count[2 * x] -= need;
        }
        return true;
    }
}
