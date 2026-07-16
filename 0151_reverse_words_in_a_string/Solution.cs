using System;
using System.Linq;

public class Solution {
    public string ReverseWords(string s) => string.Join(" ", s.Split((char[])null, StringSplitOptions.RemoveEmptyEntries).Reverse());
}