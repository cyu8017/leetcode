// LeetCode 0301 - Remove Invalid Parentheses
// https://leetcode.com/problems/remove-invalid-parentheses/

using System.Collections.Generic;

public class Solution {
    public IList<string> RemoveInvalidParentheses(string s) {
        HashSet<string> result = new();
        Queue<string> queue = new();
        HashSet<string> visited = new();
        queue.Enqueue(s);
        visited.Add(s);
        bool found = false;
        while (queue.Count > 0) {
            int levelSize = queue.Count;
            for (int step = 0; step < levelSize; step++) {
                string current = queue.Dequeue();
                if (IsValid(current)) {
                    result.Add(current);
                    found = true;
                }
                if (found) {
                    continue;
                }
                for (int index = 0; index < current.Length; index++) {
                    char ch = current[index];
                    if (ch != '(' && ch != ')') {
                        continue;
                    }
                    string next = current.Substring(0, index) + current.Substring(index + 1);
                    if (visited.Add(next)) {
                        queue.Enqueue(next);
                    }
                }
            }
        }
        return new List<string>(result);
    }

    private static bool IsValid(string text) {
        int balance = 0;
        foreach (char ch in text) {
            if (ch == '(') {
                balance++;
            } else if (ch == ')') {
                if (balance == 0) {
                    return false;
                }
                balance--;
            }
        }
        return balance == 0;
    }
}
