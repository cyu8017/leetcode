// LeetCode 3081 - Replace Question Marks in String to Minimize Its Value
// https://leetcode.com/problems/replace-question-marks-in-string-to-minimize-its-value/

using System;
using System.Collections.Generic;

public class Solution {
    public string MinimizeStringValue(string s) {
        int[] cnt = new int[26];
        int k = 0;
        foreach (char c in s) {
            if (c == '?') k++;
            else cnt[c - 'a']++;
        }
        var pq = new PriorityQueue<int, (int, int)>();
        for (int i = 0; i < 26; i++) pq.Enqueue(i, (cnt[i], i));
        int[] t = new int[k];
        for (int i = 0; i < k; i++) {
            int idx = pq.Dequeue();
            t[i] = idx;
            cnt[idx]++;
            pq.Enqueue(idx, (cnt[idx], idx));
        }
        Array.Sort(t);
        char[] arr = s.ToCharArray();
        int j = 0;
        for (int i = 0; i < arr.Length; i++) {
            if (arr[i] == '?') {
                arr[i] = (char)(t[j] + 'a');
                j++;
            }
        }
        return new string(arr);
    }
}
