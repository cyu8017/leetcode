// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        var freq = new Dictionary<int, int>();
        foreach (int x in arr) freq[x] = freq.GetValueOrDefault(x) + 1;
        var counts = freq.Values;
        return counts.Count() == counts.Distinct().Count();
    }
}
