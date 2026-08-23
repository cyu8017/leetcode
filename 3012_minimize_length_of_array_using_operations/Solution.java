// LeetCode 3012 - Minimize Length of Array Using Operations
// https://leetcode.com/problems/minimize-length-of-array-using-operations/

class Solution {
    public int minimumArrayLength(int[] nums) {
        int mi = nums[0];
        for (int x : nums) if (x < mi) mi = x;
        int cnt = 0;
        for (int x : nums) {
            if (x % mi != 0) return 1;
            if (x == mi) cnt++;
        }
        return (cnt + 1) / 2;
    }
}
