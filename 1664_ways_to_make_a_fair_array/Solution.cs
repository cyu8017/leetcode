// LeetCode 1664 - Ways to Make a Fair Array
// https://leetcode.com/problems/ways-to-make-a-fair-array/

public class Solution {
    public int WaysToMakeFair(int[] nums) {
        int te = 0, to = 0;
        for (int i = 0; i < nums.Length; i++) {
            if ((i & 1) == 0) te += nums[i];
            else to += nums[i];
        }
        int le = 0, lo = 0, ans = 0;
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i];
            if ((i & 1) == 1) to -= x;
            else te -= x;
            if (le + to == lo + te) ans++;
            if ((i & 1) == 1) lo += x;
            else le += x;
        }
        return ans;
    }
}
