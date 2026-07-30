// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<string> RemoveSubfolders(string[] folder) {
        var answer = new List<string>();
        foreach (string path in folder.OrderBy(x => x)) {
            if (answer.Count == 0 || !path.StartsWith(answer[^1] + "/")) {
                answer.Add(path);
            }
        }
        return answer;
    }
}
