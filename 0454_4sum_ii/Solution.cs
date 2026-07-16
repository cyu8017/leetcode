// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

using System.Collections.Generic;

public class Solution {
    public int FourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        Dictionary<int, int> pairSums = new();
        foreach (int a in nums1) {
            foreach (int b in nums2) {
                int sum = a + b;
                pairSums[sum] = pairSums.GetValueOrDefault(sum) + 1;
            }
        }
        int total = 0;
        foreach (int c in nums3) {
            foreach (int d in nums4) {
                total += pairSums.GetValueOrDefault(-(c + d));
            }
        }
        return total;
    }
}
