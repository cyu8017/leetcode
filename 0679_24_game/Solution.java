// LeetCode 0679 - 24 Game
// https://leetcode.com/problems/24-game/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final double EPS = 1e-6;

    public boolean judgePoint24(int[] cards) {
        List<Double> nums = new ArrayList<>();
        for (int card : cards) {
            nums.add((double) card);
        }
        return dfs(nums);
    }

    private boolean dfs(List<Double> nums) {
        if (nums.size() == 1) {
            return Math.abs(nums.get(0) - 24.0) < EPS;
        }
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = 0; j < nums.size(); ++j) {
                if (i == j) {
                    continue;
                }
                List<Double> rest = new ArrayList<>();
                for (int k = 0; k < nums.size(); ++k) {
                    if (k != i && k != j) {
                        rest.add(nums.get(k));
                    }
                }
                double a = nums.get(i);
                double b = nums.get(j);
                List<Double> candidates = new ArrayList<>();
                candidates.add(a + b);
                candidates.add(a - b);
                candidates.add(a * b);
                if (Math.abs(b) > EPS) {
                    candidates.add(a / b);
                }
                for (double value : candidates) {
                    rest.add(value);
                    if (dfs(rest)) {
                        return true;
                    }
                    rest.remove(rest.size() - 1);
                }
            }
        }
        return false;
    }
}
