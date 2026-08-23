// LeetCode 2899 - Last Visited Integers
// https://leetcode.com/problems/last-visited-integers/

using System.Collections.Generic;

public class Solution {
    public IList<int> LastVisitedIntegers(IList<int> nums) {
        var seen = new List<int>();
        var ans = new List<int>();
        int k = 0;
        foreach (int v in nums) {
            if (v != -1) {
                seen.Add(v);
                k = 0;
            } else {
                k++;
                if (k > seen.Count) ans.Add(-1);
                else ans.Add(seen[seen.Count - k]);
            }
        }
        return ans;
    }
}
