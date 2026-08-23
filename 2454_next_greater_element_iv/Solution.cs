// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

using System.Collections.Generic;

public class Solution {
    public int[] SecondGreaterElement(int[] nums) {
        int n = nums.Length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) ans[i] = -1;
        var stack1 = new List<int>();
        var stack2 = new List<int>();
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (stack2.Count > 0 && nums[stack2[stack2.Count - 1]] < x) {
                ans[stack2[stack2.Count - 1]] = x;
                stack2.RemoveAt(stack2.Count - 1);
            }
            var tmp = new List<int>();
            while (stack1.Count > 0 && nums[stack1[stack1.Count - 1]] < x) {
                tmp.Add(stack1[stack1.Count - 1]);
                stack1.RemoveAt(stack1.Count - 1);
            }
            for (int j = tmp.Count - 1; j >= 0; j--) stack2.Add(tmp[j]);
            stack1.Add(i);
        }
        return ans;
    }
}
