// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

public class Solution {
    public string RemoveDigit(string number, char digit) {
        string best = "";
        for (int i = 0; i < number.Length; i++) {
            if (number[i] == digit) {
                string cand = number.Substring(0, i) + number.Substring(i + 1);
                if (string.CompareOrdinal(cand, best) > 0) best = cand;
            }
        }
        return best;
    }
}
