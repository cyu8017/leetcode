public class Solution {
    public bool IsOneEditDistance(string s, string t) { if (System.Math.Abs(s.Length - t.Length) > 1 || s == t) return false; if (s.Length > t.Length) { var temp = s; s = t; t = temp; } int i = 0; while (i < s.Length && s[i] == t[i]) i++; return s.Length == t.Length ? s[(i + 1)..] == t[(i + 1)..] : s[i..] == t[(i + 1)..]; }
}