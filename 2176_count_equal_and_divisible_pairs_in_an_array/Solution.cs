// LeetCode 2176 - Count Equal and Divisible Pairs in an Array
// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

public class Solution {
    public int CountPairs(int[] nums, int k) {
        int ans = 0;
        for (int i = 0; i < nums.Length; i++)
            for (int j = i + 1; j < nums.Length; j++)
                if (nums[i] == nums[j] && (i * j) % k == 0) ans++;
        return ans;
    }
}
