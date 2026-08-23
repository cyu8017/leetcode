// LeetCode 3083 - Existence of a Substring in a String and Its Reverse
// https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/

public class Solution {
    public bool IsSubstringPresent(string s) {
        bool[,] st = new bool[26, 26];
        for (int i = 0; i + 1 < s.Length; i++)
            st[s[i + 1] - 'a', s[i] - 'a'] = true;
        for (int i = 0; i + 1 < s.Length; i++)
            if (st[s[i] - 'a', s[i + 1] - 'a']) return true;
        return false;
    }
}
