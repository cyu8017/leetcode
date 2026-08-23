// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

class Solution {
    public int minimumSwaps(int[] nums) {
        int n = nums.length;
        int minI = 0, maxI = 0;
        for (int i = 1; i < n; i++) {
            if (nums[i] < nums[minI]) minI = i;
            if (nums[i] >= nums[maxI]) maxI = i;
        }
        int ans = minI + (n - 1 - maxI);
        if (minI > maxI) ans--;
        return ans;
    }
}
