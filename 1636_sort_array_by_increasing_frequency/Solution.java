// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

import java.util.*;

class Solution {
    public int[] frequencySort(int[] nums) {
        Map<Integer, Integer> count = new HashMap<>();
        for (int x : nums) count.merge(x, 1, Integer::sum);
        Integer[] boxed = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(boxed, (a, b) -> {
            int ca = count.get(a), cb = count.get(b);
            return ca != cb ? ca - cb : b - a;
        });
        for (int i = 0; i < nums.length; i++) nums[i] = boxed[i];
        return nums;
    }
}
