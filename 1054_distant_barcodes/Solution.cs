// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] RearrangeBarcodes(int[] barcodes) {
        var count = new Dictionary<int, int>();
        foreach (int x in barcodes) {
            count[x] = count.GetValueOrDefault(x) + 1;
        }
        int n = barcodes.Length;
        int[] ans = new int[n];
        int i = 0;
        foreach (var kv in count.OrderByDescending(p => p.Value)) {
            for (int f = 0; f < kv.Value; f++) {
                ans[i] = kv.Key;
                i += 2;
                if (i >= n) {
                    i = 1;
                }
            }
        }
        return ans;
    }
}
