// LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
// https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

using System.Collections.Generic;

public class Solution {
    public int MaxNonOverlapping(int[] nums, int target) {
        var seen = new HashSet<int> { 0 };
        int prefix = 0, answer = 0;
        foreach (int value in nums) {
            prefix += value;
            if (seen.Contains(prefix - target)) {
                answer++;
                prefix = 0;
                seen = new HashSet<int> { 0 };
            } else {
                seen.Add(prefix);
            }
        }
        return answer;
    }
}
