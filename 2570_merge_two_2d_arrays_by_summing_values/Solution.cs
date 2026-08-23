// LeetCode 2570 - Merge Two 2D Arrays by Summing Values
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

using System.Collections.Generic;

public class Solution {
    public int[][] MergeArrays(int[][] nums1, int[][] nums2) {
        int i = 0, j = 0;
        var ans = new List<int[]>();
        while (i < nums1.Length && j < nums2.Length) {
            if (nums1[i][0] == nums2[j][0]) {
                ans.Add(new[] { nums1[i][0], nums1[i][1] + nums2[j][1] });
                i++; j++;
            } else if (nums1[i][0] < nums2[j][0]) {
                ans.Add(new[] { nums1[i][0], nums1[i][1] });
                i++;
            } else {
                ans.Add(new[] { nums2[j][0], nums2[j][1] });
                j++;
            }
        }
        while (i < nums1.Length) {
            ans.Add(new[] { nums1[i][0], nums1[i][1] });
            i++;
        }
        while (j < nums2.Length) {
            ans.Add(new[] { nums2[j][0], nums2[j][1] });
            j++;
        }
        return ans.ToArray();
    }
}
