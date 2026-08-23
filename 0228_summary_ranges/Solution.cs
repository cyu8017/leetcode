// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

using System.Collections.Generic;

public class Solution {
    public string[] SummaryRanges(int[] nums) {
        var result = new List<string>();
        int index = 0;

        while (index < nums.Length) {
            int start = nums[index];
            while (index + 1 < nums.Length && nums[index + 1] == nums[index] + 1) {
                index++;
            }
            if (start == nums[index]) {
                result.Add(start.ToString());
            } else {
                result.Add($"{start}->{nums[index]}");
            }
            index++;
        }

        return result.ToArray();
    }
}
