// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

public class Solution {
    public string[] FindWords(string[] words) {
        HashSet<char>[] rows = {
            new HashSet<char>("qwertyuiop"),
            new HashSet<char>("asdfghjkl"),
            new HashSet<char>("zxcvbnm"),
        };
        List<string> result = new();
        foreach (string word in words) {
            HashSet<char> letters = new();
            foreach (char ch in word) {
                if (char.IsLetter(ch)) {
                    letters.Add(char.ToLower(ch));
                }
            }
            foreach (HashSet<char> row in rows) {
                if (row.IsSupersetOf(letters)) {
                    result.Add(word);
                    break;
                }
            }
        }
        return result.ToArray();
    }
}
