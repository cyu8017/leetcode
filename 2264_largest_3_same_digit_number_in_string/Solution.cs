// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

public class Solution {
    public string LargestGoodInteger(string num) {
        string best = "";
        for (int i = 0; i + 2 < num.Length; i++) {
            if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
                string cand = num.Substring(i, 3);
                if (string.CompareOrdinal(cand, best) > 0) best = cand;
            }
        }
        return best;
    }
}
