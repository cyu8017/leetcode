// LeetCode 2044 - Count Number of Maximum Bitwise-OR Subsets
// https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

public class Solution {
    public int CountMaxOrSubsets(int[] nums) {
        int maxOr = 0, ans = 0;
        foreach (int x in nums) maxOr |= x;
        void Dfs(int i, int cur) {
            if (i == nums.Length) { if (cur == maxOr) ans++; return; }
            Dfs(i + 1, cur);
            Dfs(i + 1, cur | nums[i]);
        }
        Dfs(0, 0);
        return ans;
    }
}
