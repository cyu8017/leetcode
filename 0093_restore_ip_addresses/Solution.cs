// LeetCode 0093 - Restore IP Addresses
// https://leetcode.com/problems/restore-ip-addresses/

using System.Collections.Generic;

public class Solution {
    public IList<string> RestoreIpAddresses(string s) {
        var result = new List<string>();
        var path = new List<string>();
        Backtrack(s, 0, path, result);
        return result;
    }

    private void Backtrack(string s, int start, List<string> path, List<string> result) {
        if (path.Count == 4) {
            if (start == s.Length) {
                result.Add(string.Join(".", path));
            }
            return;
        }

        for (int length = 1; length <= 3; length++) {
            if (start + length > s.Length) {
                break;
            }
            string part = s.Substring(start, length);
            if ((part.StartsWith("0") && part.Length > 1) || int.Parse(part) > 255) {
                continue;
            }
            path.Add(part);
            Backtrack(s, start + length, path, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
