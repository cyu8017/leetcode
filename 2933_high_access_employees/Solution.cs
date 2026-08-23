// LeetCode 2933 - High-Access Employees
// https://leetcode.com/problems/high-access-employees/

using System.Collections.Generic;

public class Solution {
    public IList<string> FindHighAccessEmployees(IList<IList<string>> accessTimes) {
        var m = new Dictionary<string, List<int>>();
        foreach (var a in accessTimes) {
            string name = a[0], t = a[1];
            int hh = (t[0] - '0') * 10 + (t[1] - '0');
            int mm = (t[2] - '0') * 10 + (t[3] - '0');
            if (!m.ContainsKey(name)) m[name] = new List<int>();
            m[name].Add(hh * 60 + mm);
        }
        var ans = new List<string>();
        foreach (var kv in m) {
            var times = kv.Value;
            times.Sort();
            for (int i = 0; i + 2 < times.Count; i++) {
                if (times[i + 2] - times[i] < 60) {
                    ans.Add(kv.Key);
                    break;
                }
            }
        }
        ans.Sort(System.StringComparer.Ordinal);
        return ans;
    }
}
