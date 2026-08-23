// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

using System.Collections.Generic;

public class Solution {
    public long BowlSubarrays(int[] nums) {
        int n = nums.Length;
        long ans = 0;
        int[] ngr = new int[n], ngl = new int[n];
        for (int i = 0; i < n; i++) { ngr[i] = -1; ngl[i] = -1; }
        var stack = new List<int>();
        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && nums[stack[stack.Count - 1]] < nums[i]) stack.RemoveAt(stack.Count - 1);
            if (stack.Count > 0) ngr[i] = stack[stack.Count - 1];
            stack.Add(i);
        }
        stack.Clear();
        for (int i = 0; i < n; i++) {
            while (stack.Count > 0 && nums[stack[stack.Count - 1]] < nums[i]) stack.RemoveAt(stack.Count - 1);
            if (stack.Count > 0) ngl[i] = stack[stack.Count - 1];
            stack.Add(i);
        }
        for (int i = 0; i < n; i++) {
            if (ngr[i] != -1 && ngr[i] - i >= 2) ans++;
            if (ngl[i] != -1 && i - ngl[i] >= 2) ans++;
        }
        return ans;
    }
}
