// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

using System.Collections.Generic;

public class Solution {
    public int MinNumber(int[] nums1, int[] nums2) {
        var s1 = new HashSet<int>(nums1);
        var s2 = new HashSet<int>(nums2);
        int bestShared = 10;
        for (int d = 1; d <= 9; ++d) {
            if (s1.Contains(d) && s2.Contains(d) && d < bestShared) bestShared = d;
        }
        if (bestShared < 10) return bestShared;
        int m1 = 10, m2 = 10;
        foreach (int x in nums1) if (x < m1) m1 = x;
        foreach (int x in nums2) if (x < m2) m2 = x;
        if (m1 < m2) return m1 * 10 + m2;
        return m2 * 10 + m1;
    }
}
