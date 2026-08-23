// LeetCode 0219 - Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/

using System.Collections.Generic;

public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        var lastIndex = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (lastIndex.TryGetValue(nums[i], out int prev) && i - prev <= k) {
                return true;
            }
            lastIndex[nums[i]] = i;
        }
        return false;
    }
}
