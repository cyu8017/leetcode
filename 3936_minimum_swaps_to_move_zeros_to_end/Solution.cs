// LeetCode 3936 - Minimum Swaps To Move Zeros To End
// https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/

public class Solution {
    public int MinimumSwaps(int[] nums) {
        int ans = 0;
        int n = nums.Length;
        for (int i = 0, j = n - 1; i < j; i++, j--) {
            while (i < n && nums[i] != 0) i++;
            while (j > 0 && nums[j] == 0) j--;
            if (i >= j) break;
            ans++;
        }
        return ans;
    }
}
