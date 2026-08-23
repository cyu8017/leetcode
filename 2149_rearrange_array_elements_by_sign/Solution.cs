// LeetCode 2149 - Rearrange Array Elements by Sign
// https://leetcode.com/problems/rearrange-array-elements-by-sign/

public class Solution {
    public int[] RearrangeArray(int[] nums) {
        int[] ans = new int[nums.Length];
        int pos = 0, neg = 1;
        foreach (int x in nums) {
            if (x > 0) { ans[pos] = x; pos += 2; }
            else { ans[neg] = x; neg += 2; }
        }
        return ans;
    }
}
