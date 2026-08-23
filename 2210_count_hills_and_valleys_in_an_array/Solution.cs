// LeetCode 2210 - Count Hills and Valleys in an Array
// https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int CountHillValley(int[] nums) {
        var compact = new List<int> { nums[0] };
        for (int i = 1; i < nums.Length; i++)
            if (nums[i] != compact[compact.Count - 1]) compact.Add(nums[i]);
        int ans = 0;
        for (int i = 1; i + 1 < compact.Count; i++)
            if ((compact[i] > compact[i - 1] && compact[i] > compact[i + 1]) ||
                (compact[i] < compact[i - 1] && compact[i] < compact[i + 1]))
                ans++;
        return ans;
    }
}
