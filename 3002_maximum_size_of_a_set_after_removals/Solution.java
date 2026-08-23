// LeetCode 3002 - Maximum Size of a Set After Removals
// https://leetcode.com/problems/maximum-size-of-a-set-after-removals/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maximumSetSize(int[] nums1, int[] nums2) {
        Set<Integer> s1 = new HashSet<>();
        Set<Integer> s2 = new HashSet<>();
        for (int v : nums1) s1.add(v);
        for (int v : nums2) s2.add(v);
        int a = 0, b = 0, c = 0;
        for (int x : s1) if (!s2.contains(x)) a++;
        for (int x : s2) {
            if (!s1.contains(x)) b++;
            else c++;
        }
        int n = nums1.length;
        a = Math.min(a, n / 2);
        b = Math.min(b, n / 2);
        return Math.min(a + b + c, n);
    }
}
