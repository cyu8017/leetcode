// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

using System.Collections.Generic;

public class Solution {
    public int NumberOfSubarrays(int[] nums, int k) {
        var frequency = new Dictionary<int, int> { [0] = 1 };
        int odd = 0, answer = 0;
        foreach (int x in nums) {
            odd += x & 1;
            if (frequency.TryGetValue(odd - k, out int cnt)) answer += cnt;
            frequency[odd] = frequency.GetValueOrDefault(odd) + 1;
        }
        return answer;
    }
}
