// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public int NumUniqueEmails(string[] emails) {
        var normalized = new HashSet<string>();
        foreach (var email in emails) {
            int at = email.IndexOf('@');
            string local = email.Substring(0, at);
            string domain = email.Substring(at);
            int plus = local.IndexOf('+');
            if (plus >= 0) local = local.Substring(0, plus);
            var cleaned = new StringBuilder();
            foreach (char c in local) if (c != '.') cleaned.Append(c);
            normalized.Add(cleaned.ToString() + domain);
        }
        return normalized.Count;
    }
}
