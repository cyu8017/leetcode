// LeetCode 1338 - Reduce Array Size To The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public int MinSetSize(int[] arr) {
        var freq = new Dictionary<int, int>();
        foreach (int x in arr) { if (!freq.ContainsKey(x)) freq[x] = 0; freq[x]++; }
        int removed = 0, count = 0;
        foreach (int frequency in freq.Values.OrderByDescending(v => v)) {
            removed += frequency; count++;
            if (removed * 2 >= arr.Length) return count;
        }
        return 0;
    }
}
