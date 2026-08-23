// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public IList<string> RemoveComments(string[] source) {
        var result = new List<string>();
        var buffer = new StringBuilder();
        bool inBlock = false;
        foreach (string line in source) {
            int i = 0;
            while (i < line.Length) {
                if (inBlock) {
                    if (i + 1 < line.Length && line[i] == '*' && line[i + 1] == '/') { inBlock = false; i += 2; }
                    else i++;
                } else if (i + 1 < line.Length && line[i] == '/' && line[i + 1] == '*') { inBlock = true; i += 2; }
                else if (i + 1 < line.Length && line[i] == '/' && line[i + 1] == '/') break;
                else buffer.Append(line[i++]);
            }
            if (!inBlock && buffer.Length > 0) {
                result.Add(buffer.ToString());
                buffer.Clear();
            }
        }
        return result;
    }
}
