// LeetCode 1604 - Alert Using Same Key-Card Three or More Times in a One Hour Period
// https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> AlertNames(string[] keyName, string[] keyTime) {
        var times = new Dictionary<string, List<int>>();
        for (int i = 0; i < keyName.Length; i++) {
            if (!times.ContainsKey(keyName[i])) times[keyName[i]] = new List<int>();
            var parts = keyTime[i].Split(':');
            times[keyName[i]].Add(int.Parse(parts[0]) * 60 + int.Parse(parts[1]));
        }
        var ans = new List<string>();
        foreach (var kv in times) {
            var a = kv.Value;
            a.Sort();
            for (int i = 0; i + 2 < a.Count; i++) {
                if (a[i + 2] - a[i] <= 60) {
                    ans.Add(kv.Key);
                    break;
                }
            }
        }
        ans.Sort(StringComparer.Ordinal);
        return ans;
    }
}
