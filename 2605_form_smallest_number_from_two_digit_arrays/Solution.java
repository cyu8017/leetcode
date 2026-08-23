// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minNumber(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();
        for (int x : nums1) s1.add(x);
        for (int x : nums2) s2.add(x);
        int common = 10;
        for (int x : s1) if (s2.contains(x) && x < common) common = x;
        if (common < 10) return common;
        int a = 10, b = 10;
        for (int x : nums1) if (x < a) a = x;
        for (int x : nums2) if (x < b) b = x;
        return Math.min(a * 10 + b, b * 10 + a);
    }
}
