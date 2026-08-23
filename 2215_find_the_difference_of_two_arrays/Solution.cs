// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> FindDifference(int[] nums1, int[] nums2) {
        var s1 = new HashSet<int>(nums1);
        var s2 = new HashSet<int>(nums2);
        var a = new List<int>();
        var b = new List<int>();
        foreach (int x in s1) if (!s2.Contains(x)) a.Add(x);
        foreach (int x in s2) if (!s1.Contains(x)) b.Add(x);
        return new List<IList<int>> { a, b };
    }
}
