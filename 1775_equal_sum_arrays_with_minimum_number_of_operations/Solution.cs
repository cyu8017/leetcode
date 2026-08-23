// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

using System;
using System.Linq;

public class Solution {
    public int MinOperations(int[] nums1, int[] nums2) {
        if (nums1.Length * 6 < nums2.Length || nums2.Length * 6 < nums1.Length) {
            return -1;
        }
        int s1 = nums1.Sum();
        int s2 = nums2.Sum();
        if (s1 == s2) {
            return 0;
        }
        int[] big = nums1;
        int[] small = nums2;
        if (s1 < s2) {
            big = nums2;
            small = nums1;
            (s1, s2) = (s2, s1);
        }
        int diff = s1 - s2;
        var gains = big.Select(x => x - 1).Concat(small.Select(x => 6 - x)).ToArray();
        Array.Sort(gains);
        Array.Reverse(gains);
        int ops = 0;
        foreach (int gain in gains) {
            if (diff <= 0) {
                break;
            }
            diff -= gain;
            ops++;
        }
        return diff <= 0 ? ops : -1;
    }
}
