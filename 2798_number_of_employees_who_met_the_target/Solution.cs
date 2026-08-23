// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

public class Solution {
    public int NumberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int ans = 0;
        foreach (int h in hours) if (h >= target) ans++;
        return ans;
    }
}
