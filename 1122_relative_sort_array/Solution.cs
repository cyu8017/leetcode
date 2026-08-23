// LeetCode 1122 - Relative Sort Array
// https://leetcode.com/problems/relative-sort-array/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] RelativeSortArray(int[] arr1, int[] arr2) {
        var count = new Dictionary<int, int>();
        foreach (int x in arr1) {
            if (!count.ContainsKey(x)) count[x] = 0;
            count[x]++;
        }
        var ans = new List<int>();
        foreach (int x in arr2) {
            while (count.ContainsKey(x) && count[x]-- > 0) {
                ans.Add(x);
            }
            count.Remove(x);
        }
        foreach (var kv in count.OrderBy(p => p.Key)) {
            for (int i = 0; i < kv.Value; i++) {
                ans.Add(kv.Key);
            }
        }
        return ans.ToArray();
    }
}
