// LeetCode 3636 - Threshold Majority Queries
// https://leetcode.com/problems/threshold-majority-queries/

using System.Collections.Generic;

public class Solution {
    public int[] SubarrayMajority(int[] nums, int[][] queries) {
        int[] ans = new int[queries.Length];
        for (int qi = 0; qi < queries.Length; qi++) {
            int l = queries[qi][0], r = queries[qi][1], thresh = queries[qi][2];
            var freq = new Dictionary<int, int>();
            for (int i = l; i <= r; i++) {
                if (!freq.ContainsKey(nums[i])) freq[nums[i]] = 0;
                freq[nums[i]]++;
            }
            int bestVal = -1, bestCnt = 0;
            foreach (var kv in freq) {
                int v = kv.Key, c = kv.Value;
                if (c >= thresh && (c > bestCnt || (c == bestCnt && (bestVal == -1 || v < bestVal)))) {
                    bestCnt = c;
                    bestVal = v;
                }
            }
            ans[qi] = bestVal;
        }
        return ans;
    }
}
