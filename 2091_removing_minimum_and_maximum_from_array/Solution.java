// LeetCode 2091 - Removing Minimum and Maximum From Array
// https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

class Solution {
    public int minimumDeletions(int[] nums) {
        int n = nums.length, mi = 0, ma = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] < nums[mi]) mi = i;
            if (nums[i] > nums[ma]) ma = i;
        }
        if (mi > ma) { int t = mi; mi = ma; ma = t; }
        return Math.min(ma + 1, Math.min(n - mi, mi + 1 + n - ma));
    }
}
