// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] secondGreaterElement(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        var stack1 = new ArrayList<Integer>();
        var stack2 = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (stack2.size() > 0 && nums[stack2.get(stack2.size() - 1)] < x) {
                ans[stack2.get(stack2.size() - 1)] = x;
                stack2.remove(stack2.size() - 1);
            }
            var tmp = new ArrayList<Integer>();
            while (stack1.size() > 0 && nums[stack1.get(stack1.size() - 1)] < x) {
                tmp.add(stack1.get(stack1.size() - 1));
                stack1.remove(stack1.size() - 1);
            }
            for (int j = tmp.size() - 1; j >= 0; j--) stack2.add(tmp.get(j));
            stack1.add(i);
        }
        return ans;
    }
}
