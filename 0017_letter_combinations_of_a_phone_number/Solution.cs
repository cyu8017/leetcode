// LeetCode 0017 - Letter Combinations of a Phone Number
// https://leetcode.com/problems/letter-combinations-of-a-phone-number/

public class Solution {
    private static readonly string[] Mapping = {
        "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
    };

    public IList<string> LetterCombinations(string digits) {
        var result = new List<string>();
        if (digits.Length == 0) {
            return result;
        }
        Backtrack(digits, 0, new List<char>(), result);
        return result;
    }

    private void Backtrack(string digits, int index, List<char> path, IList<string> result) {
        if (index == digits.Length) {
            result.Add(new string(path.ToArray()));
            return;
        }
        foreach (char ch in Mapping[digits[index] - '0']) {
            path.Add(ch);
            Backtrack(digits, index + 1, path, result);
            path.RemoveAt(path.Count - 1);
        }
    }
}
