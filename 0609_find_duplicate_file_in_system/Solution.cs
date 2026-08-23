// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

using System.Collections.Generic;

public class Solution {
    public IList<IList<string>> FindDuplicate(string[] paths) {
        var contentToPaths = new Dictionary<string, List<string>>();
        foreach (string entry in paths) {
            string[] parts = entry.Split(' ');
            string directory = parts[0];
            for (int i = 1; i < parts.Length; ++i) {
                string fileInfo = parts[i];
                int open = fileInfo.IndexOf('(');
                string name = fileInfo.Substring(0, open);
                string content = fileInfo.Substring(open + 1, fileInfo.Length - open - 2);
                if (!contentToPaths.ContainsKey(content)) contentToPaths[content] = new List<string>();
                contentToPaths[content].Add(directory + "/" + name);
            }
        }
        var result = new List<IList<string>>();
        foreach (var group in contentToPaths.Values) {
            if (group.Count > 1) result.Add(group);
        }
        return result;
    }
}
