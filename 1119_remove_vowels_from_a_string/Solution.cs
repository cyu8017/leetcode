// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

using System.Text;

public class Solution {
    public string RemoveVowels(string s) {
        var ans = new StringBuilder();
        foreach (char ch in s) {
            if (ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u') {
                ans.Append(ch);
            }
        }
        return ans.ToString();
    }
}
