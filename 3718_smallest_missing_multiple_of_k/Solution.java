// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int missingMultiple(int[] nums, int k) {
        Set<Integer> s = new HashSet<>();
        for (int x : nums) s.add(x);
        for (int i = 1; ; i++) {
            int x = k * i;
            if (!s.contains(x)) return x;
        }
    }
}
