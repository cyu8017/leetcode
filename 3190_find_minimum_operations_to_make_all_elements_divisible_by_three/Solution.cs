// LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
// https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

public class Solution {
    public int MinimumOperations(int[] nums) {
        int ans = 0;
        foreach (int x in nums) if (x % 3 != 0) ans++;
        return ans;
    }
}
