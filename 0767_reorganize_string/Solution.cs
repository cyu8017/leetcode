// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ReorganizeString(string s) {
        int[] freq = new int[26];
        foreach (char ch in s) freq[ch - 'a']++;
        var heap = new PriorityQueue<(int count, char ch), int>();
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) heap.Enqueue((freq[i], (char)('a' + i)), -freq[i]);
        }
        if (heap.Count > 0 && heap.Peek().count > (s.Length + 1) / 2) return "";
        var result = new StringBuilder();
        while (heap.Count >= 2) {
            var (c1, a) = heap.Dequeue();
            var (c2, b) = heap.Dequeue();
            result.Append(a);
            result.Append(b);
            if (--c1 > 0) heap.Enqueue((c1, a), -c1);
            if (--c2 > 0) heap.Enqueue((c2, b), -c2);
        }
        if (heap.Count > 0) result.Append(heap.Peek().ch);
        return result.ToString();
    }
}
