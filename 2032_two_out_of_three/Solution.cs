// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

using System.Collections.Generic;

public class Solution {
    public int[] TwoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        var s0 = new HashSet<int>(nums1);
        var s1 = new HashSet<int>(nums2);
        var s2 = new HashSet<int>(nums3);
        var ans = new List<int>();
        for (int v = 1; v <= 100; v++) {
            int c = (s0.Contains(v) ? 1 : 0) + (s1.Contains(v) ? 1 : 0) + (s2.Contains(v) ? 1 : 0);
            if (c >= 2) ans.Add(v);
        }
        return ans.ToArray();
    }
}
