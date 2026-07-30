// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

using System.Collections.Generic;
public class Solution {
    public string[] GetFolderNames(string[] names) {
        var used = new Dictionary<string, int>();
        var ans = new string[names.Length];
        for (int i = 0; i < names.Length; i++) {
            string name = names[i], candidate;
            if (!used.ContainsKey(name)) candidate = name;
            else {
                int k = used[name];
                while (used.ContainsKey($"{name}({k})")) k++;
                candidate = $"{name}({k})";
                used[name] = k + 1;
            }
            used[candidate] = 1;
            ans[i] = candidate;
        }
        return ans;
    }
}
