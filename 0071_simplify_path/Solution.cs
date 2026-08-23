// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

public class Solution {
    public string SimplifyPath(string path) {
        var stack = new List<string>();

        foreach (var part in path.Split('/')) {
            if (part.Length == 0 || part == ".") {
                continue;
            }
            if (part == "..") {
                if (stack.Count > 0) {
                    stack.RemoveAt(stack.Count - 1);
                }
            } else {
                stack.Add(part);
            }
        }

        return "/" + string.Join("/", stack);
    }
}
