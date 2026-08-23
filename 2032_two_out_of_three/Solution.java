// LeetCode 2032 - Two Out of Three
// https://leetcode.com/problems/two-out-of-three/

import java.util.*;

class Solution {
    public int[] twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        Set<Integer> s0 = new HashSet<>(), s1 = new HashSet<>(), s2 = new HashSet<>();
        for (int v : nums1) s0.add(v);
        for (int v : nums2) s1.add(v);
        for (int v : nums3) s2.add(v);
        List<Integer> ans = new ArrayList<>();
        for (int v = 1; v <= 100; v++) {
            int c = (s0.contains(v) ? 1 : 0) + (s1.contains(v) ? 1 : 0) + (s2.contains(v) ? 1 : 0);
            if (c >= 2) ans.add(v);
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}
