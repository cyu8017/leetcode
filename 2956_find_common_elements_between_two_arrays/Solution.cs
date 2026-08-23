// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

using System.Collections.Generic;

public class Solution {
    public int[] FindIntersectionValues(int[] nums1, int[] nums2) {
        var s1 = new HashSet<int>(nums1);
        var s2 = new HashSet<int>(nums2);
        int a = 0, b = 0;
        foreach (int v in nums1) if (s2.Contains(v)) a++;
        foreach (int v in nums2) if (s1.Contains(v)) b++;
        return new int[] { a, b };
    }
}
