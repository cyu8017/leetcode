// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] getSneakyNumbers(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        List<Integer> ans = new ArrayList<>();
        for (int x : nums) {
            if (!seen.add(x)) ans.add(x);
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }
}
