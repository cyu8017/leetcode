// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

using System.Collections.Generic;

public class Solution {
    public long MaxScore(int[] nums) {
        var stk = new List<int>();
        for (int i = 0; i < nums.Length; i++) {
            while (stk.Count > 0 && nums[stk[stk.Count - 1]] <= nums[i]) stk.RemoveAt(stk.Count - 1);
            stk.Add(i);
        }
        long ans = 0;
        int cur = 0;
        foreach (int j in stk) {
            ans += (long)(j - cur) * nums[j];
            cur = j;
        }
        return ans;
    }
}
