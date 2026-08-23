// LeetCode 3432 - Count Partitions with Even Sum Difference
// https://leetcode.com/problems/count-partitions-with-even-sum-difference/

public class Solution {
    public int CountPartitions(int[] nums) {
        int total = 0;
        foreach (int x in nums) total += x;
        int ans = 0, left = 0;
        for (int i = 0; i < nums.Length - 1; i++) {
            left += nums[i];
            if ((left - (total - left)) % 2 == 0) ans++;
        }
        return ans;
    }
}
