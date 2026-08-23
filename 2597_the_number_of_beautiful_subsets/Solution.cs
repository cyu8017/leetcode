// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

using System.Collections.Generic;

public class Solution {
    public int BeautifulSubsets(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) freq[x] = freq.GetValueOrDefault(x, 0) + 1;
        var groups = new Dictionary<int, List<int>>();
        foreach (var kv in freq) {
            int rem = kv.Key % k;
            if (!groups.ContainsKey(rem)) groups[rem] = new List<int>();
            groups[rem].Add(kv.Key);
        }
        int ans = 1;
        foreach (var vals in groups.Values) {
            vals.Sort();
            int prevTake = 0, prevSkip = 1;
            int prevVal = int.MinValue / 2;
            foreach (int v in vals) {
                int ways = 1;
                for (int i = 0; i < freq[v]; ++i) ways *= 2;
                ways--;
                int skip = prevTake + prevSkip;
                int take = ways * prevSkip;
                if (prevVal + k != v) take += ways * prevTake;
                prevTake = take;
                prevSkip = skip;
                prevVal = v;
            }
            ans *= prevTake + prevSkip;
        }
        return ans - 1;
    }
}
