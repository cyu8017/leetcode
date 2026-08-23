// LeetCode 0299 - Bulls and Cows
// https://leetcode.com/problems/bulls-and-cows/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string GetHint(string secret, string guess) {
        int bulls = 0;
        var secretCounts = new Dictionary<char, int>();
        var guessCounts = new Dictionary<char, int>();
        for (int index = 0; index < secret.Length; index++) {
            char secretDigit = secret[index];
            char guessDigit = guess[index];
            if (secretDigit == guessDigit) {
                bulls++;
            } else {
                secretCounts[secretDigit] = secretCounts.GetValueOrDefault(secretDigit) + 1;
                guessCounts[guessDigit] = guessCounts.GetValueOrDefault(guessDigit) + 1;
            }
        }
        int cows = guessCounts.Sum(entry => System.Math.Min(entry.Value, secretCounts.GetValueOrDefault(entry.Key)));
        return $"{bulls}A{cows}B";
    }
}
