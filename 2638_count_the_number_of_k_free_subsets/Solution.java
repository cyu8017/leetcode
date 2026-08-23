// LeetCode 2638 - Count the Number of K-Free Subsets
// https://leetcode.com/problems/count-the-number-of-k-free-subsets/

import java.util.*;

class Solution {
    public long countTheNumOfKFreeSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        Map<Integer, List<Integer>> groups = new HashMap<>();
        for (int x : nums) {
            groups.computeIfAbsent(x % k, z -> new ArrayList<>()).add(x);
        }
        long ans = 1;
        for (List<Integer> g : groups.values()) {
            int prevVal = -1;
            long prevTake = 0, prevSkip = 1;
            for (int v : g) {
                long take, skip = prevTake + prevSkip;
                if (prevVal + k == v) take = prevSkip;
                else take = prevTake + prevSkip;
                prevTake = take;
                prevSkip = skip;
                prevVal = v;
            }
            ans *= prevTake + prevSkip;
        }
        return ans;
    }
}
