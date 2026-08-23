// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public int CountDistinct(int[] nums, int k, int p) {
        int n = nums.Length;
        var seen = new HashSet<string>();
        for (int i = 0; i < n; i++) {
            int div = 0;
            var key = new StringBuilder();
            for (int j = i; j < n; j++) {
                if (nums[j] % p == 0) div++;
                if (div > k) break;
                key.Append(nums[j] + 1).Append(',');
                seen.Add(key.ToString());
            }
        }
        return seen.Count;
    }
}
