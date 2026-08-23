// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(n, 2, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int remain, int start, List<Integer> path, List<List<Integer>> result) {
        if (start > remain) {
            if (path.size() > 1) {
                result.add(new ArrayList<>(path));
            }
            return;
        }

        for (int factor = start; factor * factor <= remain; factor++) {
            if (remain % factor == 0) {
                path.add(factor);
                backtrack(remain / factor, factor, path, result);
                path.remove(path.size() - 1);
            }
        }

        if (!path.isEmpty()) {
            path.add(remain);
            if (path.size() > 1) {
                result.add(new ArrayList<>(path));
            }
            path.remove(path.size() - 1);
        }
    }
}
