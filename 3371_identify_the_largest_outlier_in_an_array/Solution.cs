// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

using System.Collections.Generic;

public class Solution {
    public int GetLargestOutlier(int[] nums) {
        int sum = 0;
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) {
            sum += x;
            if (!freq.ContainsKey(x)) freq[x] = 0;
            freq[x]++;
        }
        int ans = int.MinValue;
        foreach (int x in nums) {
            freq[x]--;
            int rem = sum - x;
            if (rem % 2 == 0) {
                int cand = rem / 2;
                if (freq.TryGetValue(cand, out int f) && f > 0 && x > ans) ans = x;
            }
            freq[x]++;
        }
        return ans;
    }
}
