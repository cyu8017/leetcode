// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minImpossibleOR(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int x : nums) set.add(x);
        int x = 1;
        while (set.contains(x)) x <<= 1;
        return x;
    }
}
