// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

using System.Collections.Generic;

public class Solution {
    public IList<int> Intersection(int[][] nums) {
        var freq = new Dictionary<int, int>();
        foreach (var arr in nums) {
            var seen = new HashSet<int>();
            foreach (int x in arr) {
                if (seen.Add(x)) {
                    freq.TryGetValue(x, out int c);
                    freq[x] = c + 1;
                }
            }
        }
        var ans = new List<int>();
        foreach (var kv in freq) if (kv.Value == nums.Length) ans.Add(kv.Key);
        ans.Sort();
        return ans;
    }
}
