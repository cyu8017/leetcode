// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

using System;
using System.Collections.Generic;

public class Solution {
    public string SortVowels(string s) {
        bool IsVowel(char c) =>
            c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
            c=='A'||c=='E'||c=='I'||c=='O'||c=='U';
        var vowels = new List<char>();
        foreach (char c in s) if (IsVowel(c)) vowels.Add(c);
        vowels.Sort();
        char[] arr = s.ToCharArray();
        int vi = 0;
        for (int i = 0; i < arr.Length; i++) if (IsVowel(arr[i])) arr[i] = vowels[vi++];
        return new string(arr);
    }
}
