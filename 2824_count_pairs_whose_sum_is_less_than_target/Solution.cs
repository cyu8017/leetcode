// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

using System.Collections.Generic;

public class Solution {
    public int CountPairs(IList<int> nums, int target) {
        int ans = 0;
        for (int i = 0; i < nums.Count; i++)
            for (int j = i + 1; j < nums.Count; j++)
                if (nums[i] + nums[j] < target) ans++;
        return ans;
    }
}
