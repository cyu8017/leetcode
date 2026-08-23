// LeetCode 2023 - Number of Pairs of Strings With Concatenation Equal to Target
// https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

class Solution {
    public int numOfPairs(String[] nums, String target) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++)
            for (int j = 0; j < nums.length; j++)
                if (i != j && (nums[i] + nums[j]).equals(target)) ans++;
        return ans;
    }
}
