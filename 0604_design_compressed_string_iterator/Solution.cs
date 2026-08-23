// LeetCode 0604 - Design Compressed String Iterator
// https://leetcode.com/problems/design-compressed-string-iterator/

using System.Collections.Generic;

public class StringIterator {
    private readonly List<char> chars = new();
    private readonly List<int> counts = new();
    private int index = 0;

    public StringIterator(string compressedString) {
        int n = compressedString.Length, i = 0;
        while (i < n) {
            char ch = compressedString[i++];
            int j = i;
            while (j < n && compressedString[j] >= '0' && compressedString[j] <= '9') ++j;
            chars.Add(ch);
            counts.Add(int.Parse(compressedString.Substring(i, j - i)));
            i = j;
        }
    }

    public char Next() {
        if (!HasNext()) return ' ';
        char ch = chars[index];
        --counts[index];
        if (counts[index] == 0) ++index;
        return ch;
    }

    public bool HasNext() => index < chars.Count;
}
