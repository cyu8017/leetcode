// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public int UniqueEmailGroups(string[] emails) {
        var st = new HashSet<string>();
        foreach (var email in emails) {
            int at = email.IndexOf('@');
            string local = email.Substring(0, at);
            string domain = email.Substring(at + 1).ToLowerInvariant();
            int plus = local.IndexOf('+');
            if (plus >= 0) local = local.Substring(0, plus);
            var cleaned = new StringBuilder();
            foreach (char c in local) if (c != '.') cleaned.Append(char.ToLowerInvariant(c));
            st.Add(cleaned.ToString() + domain);
        }
        return st.Count;
    }
}
