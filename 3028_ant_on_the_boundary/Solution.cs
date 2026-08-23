// LeetCode 3028 - Ant on the Boundary
// https://leetcode.com/problems/ant-on-the-boundary/

public class Solution {
    public int ReturnToBoundaryCount(int[] nums) {
        int s = 0, ans = 0;
        foreach (int x in nums) {
            s += x;
            if (s == 0) ans++;
        }
        return ans;
    }
}
