// LeetCode 0888 - Fair Candy Swap
// https://leetcode.com/problems/fair-candy-swap/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] FairCandySwap(int[] aliceSizes, int[] bobSizes) {
        int diff = (aliceSizes.Sum() - bobSizes.Sum()) / 2;
        var bob = new HashSet<int>(bobSizes);
        foreach (int a in aliceSizes) {
            if (bob.Contains(a - diff)) return new[] { a, a - diff };
        }
        return new int[0];
    }
}
