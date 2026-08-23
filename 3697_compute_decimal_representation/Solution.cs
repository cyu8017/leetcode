// LeetCode 3697 - Compute Decimal Representation
// https://leetcode.com/problems/compute-decimal-representation/

using System.Collections.Generic;

public class Solution {
    public int[] DecimalRepresentation(int n) {
        var ans = new List<int>();
        int p = 1;
        while (n > 0) {
            int v = n % 10;
            n /= 10;
            if (v != 0) ans.Add(p * v);
            p *= 10;
        }
        ans.Reverse();
        return ans.ToArray();
    }
}
