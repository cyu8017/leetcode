// LeetCode 0471 - Encode String with Shortest Length
// https://leetcode.com/problems/encode-string-with-shortest-length/

public class Solution {
    public string Encode(string s) {
        int length = s.Length;
        string[] dp = new string[length + 1];

        for (int index = 1; index <= length; index++) {
            dp[index] = EncodeWord(s[..index]);
            for (int split = 1; split < index; split++) {
                string candidate = dp[index - split] + EncodeWord(s[(index - split)..index]);
                if (candidate.Length < dp[index].Length
                    || (candidate.Length == dp[index].Length && string.CompareOrdinal(candidate, dp[index]) < 0)) {
                    dp[index] = candidate;
                }
            }
        }
        return dp[length];
    }

    private static string EncodeWord(string word) {
        int size = word.Length;
        string best = word;
        for (int unitLength = 1; unitLength <= size / 2; unitLength++) {
            if (size % unitLength != 0) {
                continue;
            }
            string unit = word[..unitLength];
            if (string.Concat(Enumerable.Repeat(unit, size / unitLength)) == word) {
                string encoded = $"{size / unitLength}[{unit}]";
                if (encoded.Length < best.Length
                    || (encoded.Length == best.Length && string.CompareOrdinal(encoded, best) < 0)) {
                    best = encoded;
                }
            }
        }
        return best;
    }
}
