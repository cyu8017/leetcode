// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<List<Integer>> findSubsequences(int[] nums) {
        Set<List<Integer>> result = new HashSet<>();
        backtrack(nums, 0, new ArrayList<>(), result);
        List<List<Integer>> sorted = new ArrayList<>(result);
        sorted.sort((left, right) -> {
            int limit = Math.min(left.size(), right.size());
            for (int index = 0; index < limit; index++) {
                int compare = left.get(index).compareTo(right.get(index));
                if (compare != 0) {
                    return compare;
                }
            }
            return Integer.compare(left.size(), right.size());
        });
        return sorted;
    }

    private void backtrack(int[] nums, int start, List<Integer> path, Set<List<Integer>> result) {
        if (path.size() >= 2) {
            result.add(new ArrayList<>(path));
        }
        Set<Integer> used = new HashSet<>();
        for (int index = start; index < nums.length; index++) {
            if (used.contains(nums[index])) {
                continue;
            }
            if (!path.isEmpty() && nums[index] < path.get(path.size() - 1)) {
                continue;
            }
            used.add(nums[index]);
            path.add(nums[index]);
            backtrack(nums, index + 1, path, result);
            path.remove(path.size() - 1);
        }
    }
}
