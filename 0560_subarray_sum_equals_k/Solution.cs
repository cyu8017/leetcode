// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

using System.Collections.Generic;

public class Solution {
    public int SubarraySum(int[] nums, int k) {
        var counts = new Dictionary<int, int> { [0] = 1 };
        int prefix = 0;
        int answer = 0;
        foreach (int num in nums) {
            prefix += num;
            if (counts.TryGetValue(prefix - k, out int c)) answer += c;
            counts.TryGetValue(prefix, out int cur);
            counts[prefix] = cur + 1;
        }
        return answer;
    }
}
