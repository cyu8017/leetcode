// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(1, k, n, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(
        int start,
        int k,
        int remaining,
        List<Integer> path,
        List<List<Integer>> result
    ) {
        if (path.size() == k) {
            if (remaining == 0) {
                result.add(new ArrayList<>(path));
            }
            return;
        }
        if (remaining <= 0 || path.size() >= k) {
            return;
        }

        for (int num = start; num <= 9; num++) {
            if (num > remaining) {
                break;
            }
            path.add(num);
            backtrack(num + 1, k, remaining - num, path, result);
            path.remove(path.size() - 1);
        }
    }
}
