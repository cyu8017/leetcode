// LeetCode 1481 - Least Number Of Unique Integers After K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int FindLeastNumOfUniqueInts(int[] arr, int k) {
        var freq = new Dictionary<int, int>();
        foreach (int x in arr) { if (!freq.ContainsKey(x)) freq[x] = 0; freq[x]++; }
        var counts = freq.Values.OrderBy(v => v).ToList();
        int removed = 0;
        foreach (int count in counts) {
            if (k < count) break;
            k -= count; removed++;
        }
        return counts.Count - removed;
    }
}
