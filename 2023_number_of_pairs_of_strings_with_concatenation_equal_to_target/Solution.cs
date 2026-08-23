// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

public class Solution {
    public int NumOfPairs(string[] nums, string target) {
        int ans = 0;
        for (int i = 0; i < nums.Length; i++)
            for (int j = 0; j < nums.Length; j++)
                if (i != j && nums[i] + nums[j] == target) ans++;
        return ans;
    }
}
