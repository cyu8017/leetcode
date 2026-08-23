// LeetCode 2824 - Count Pairs Whose Sum is Less than Target
// https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int countPairs(List<Integer> nums, int target) {
        int ans = 0;
        for (int i = 0; i < nums.size(); i++)
            for (int j = i + 1; j < nums.size(); j++)
                if (nums.get(i) + nums.get(j) < target) ans++;
        return ans;
    }
}
