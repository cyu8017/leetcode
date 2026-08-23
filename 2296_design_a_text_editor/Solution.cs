// LeetCode 2296 - Design a Text Editor
// https://leetcode.com/problems/design-a-text-editor/

using System;
using System.Collections.Generic;
using System.Text;

public class TextEditor {
    List<char> left = new List<char>();
    List<char> right = new List<char>();

    string Suffix() {
        int start = Math.Max(0, left.Count - 10);
        var sb = new StringBuilder();
        for (int i = start; i < left.Count; i++) sb.Append(left[i]);
        return sb.ToString();
    }

    public TextEditor() {}

    public void AddText(string text) {
        foreach (char c in text) left.Add(c);
    }

    public int DeleteText(int k) {
        int deleted = 0;
        while (k > 0 && left.Count > 0) { left.RemoveAt(left.Count - 1); k--; deleted++; }
        return deleted;
    }

    public string CursorLeft(int k) {
        while (k > 0 && left.Count > 0) {
            right.Add(left[left.Count - 1]);
            left.RemoveAt(left.Count - 1);
            k--;
        }
        return Suffix();
    }

    public string CursorRight(int k) {
        while (k > 0 && right.Count > 0) {
            left.Add(right[right.Count - 1]);
            right.RemoveAt(right.Count - 1);
            k--;
        }
        return Suffix();
    }
}
