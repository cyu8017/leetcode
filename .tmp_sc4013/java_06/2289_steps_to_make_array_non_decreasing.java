// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int totalSteps(int[] nums) {
        List<int[]> stack = new ArrayList<>();
        int ans = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            int steps = 0;
            while (!stack.isEmpty() && nums[i] > stack.get(stack.size() - 1)[0]) {
                steps = Math.max(steps, stack.get(stack.size() - 1)[1]);
                stack.remove(stack.size() - 1);
                steps++;
            }
            ans = Math.max(ans, steps);
            stack.add(new int[] { nums[i], steps });
        }
        return ans;
    }
}
