// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/

using System.Collections.Generic;

public class Solution {
    public bool IsTransformable(string s, string t) {
        var positions = new Queue<int>[10];
        for (int d = 0; d < 10; d++) positions[d] = new Queue<int>();
        for (int i = 0; i < s.Length; i++) positions[s[i] - '0'].Enqueue(i);
        foreach (char ch in t) {
            int d = ch - '0';
            if (positions[d].Count == 0) return false;
            int index = positions[d].Peek();
            for (int smaller = 0; smaller < d; smaller++) {
                if (positions[smaller].Count > 0 && positions[smaller].Peek() < index)
                    return false;
            }
            positions[d].Dequeue();
        }
        return true;
    }
}
