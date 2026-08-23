// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

using System.Collections.Generic;

public class Solution {
    public int LargestInteger(int num) {
        var digits = new List<int>();
        for (int x = num; x > 0; x /= 10) digits.Insert(0, x % 10);
        var even = new List<int>();
        var odd = new List<int>();
        foreach (int d in digits) {
            if (d % 2 == 0) even.Add(d);
            else odd.Add(d);
        }
        even.Sort((a, b) => b.CompareTo(a));
        odd.Sort((a, b) => b.CompareTo(a));
        int ei = 0, oi = 0, ans = 0;
        foreach (int d in digits) {
            if (d % 2 == 0) ans = ans * 10 + even[ei++];
            else ans = ans * 10 + odd[oi++];
        }
        return ans;
    }
}
