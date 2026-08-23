// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();
        for (int v : nums1) s1.add(v);
        for (int v : nums2) s2.add(v);
        int a = 0, b = 0;
        for (int v : nums1) if (s2.contains(v)) a++;
        for (int v : nums2) if (s1.contains(v)) b++;
        return new int[] { a, b };
    }
}
