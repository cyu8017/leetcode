// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> AccountsMerge(IList<IList<string>> accounts) {
        var parent = new Dictionary<string, string>();
        var emailName = new Dictionary<string, string>();

        string Find(string x) {
            if (!parent.ContainsKey(x)) parent[x] = x;
            while (parent[x] != x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        }
        void Unite(string a, string b) => parent[Find(a)] = Find(b);

        foreach (var account in accounts) {
            string name = account[0], first = account[1];
            for (int i = 1; i < account.Count; i++) {
                string email = account[i];
                if (!parent.ContainsKey(email)) parent[email] = email;
                emailName[email] = name;
                Unite(first, email);
            }
        }

        var groups = new Dictionary<string, List<string>>();
        foreach (string email in parent.Keys) {
            string root = Find(email);
            if (!groups.ContainsKey(root)) groups[root] = new List<string>();
            groups[root].Add(email);
        }

        var result = new List<IList<string>>();
        foreach (var emails in groups.Values) {
            emails.Sort(System.StringComparer.Ordinal);
            var row = new List<string> { emailName[emails[0]] };
            row.AddRange(emails);
            result.Add(row);
        }
        return result;
    }
}
