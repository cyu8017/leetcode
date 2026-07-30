// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than Or Equal To Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

using System.Collections.Generic;
public class Solution {
    public int LongestSubarray(int[] nums, int limit) {
        var low = new LinkedList<int>(); var high = new LinkedList<int>();
        int left = 0, answer = 0;
        for (int right = 0; right < nums.Length; right++) {
            while (low.Count > 0 && nums[low.Last.Value] > nums[right]) low.RemoveLast();
            while (high.Count > 0 && nums[high.Last.Value] < nums[right]) high.RemoveLast();
            low.AddLast(right); high.AddLast(right);
            while (nums[high.First.Value] - nums[low.First.Value] > limit) {
                left++;
                if (low.First.Value < left) low.RemoveFirst();
                if (high.First.Value < left) high.RemoveFirst();
            }
            answer = System.Math.Max(answer, right - left + 1);
        }
        return answer;
    }
}
