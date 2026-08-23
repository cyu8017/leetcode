// LeetCode 2216 - Minimum Deletions to Make Array Beautiful
// https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

public class Solution {
    public int MinDeletion(int[] nums) {
        int ans = 0, i = 0, n = nums.Length;
        while (i + 1 < n) {
            if (nums[i] == nums[i + 1]) { ans++; i++; }
            else i += 2;
        }
        if ((n - ans) % 2 != 0) ans++;
        return ans;
    }
}
