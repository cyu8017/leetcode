// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

public class Solution {
    public string CapitalizeTitle(string title) {
        var parts = title.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        for (int i = 0; i < parts.Length; i++) {
            string w = parts[i].ToLowerInvariant();
            if (w.Length > 2) w = char.ToUpperInvariant(w[0]) + w.Substring(1);
            parts[i] = w;
        }
        return string.Join(" ", parts);
    }
}
