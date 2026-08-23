// LeetCode 2283 - Check if Number Has Equal Digit Count and Digit Value
// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/

public class Solution {
    public bool DigitCount(string num) {
        int[] cnt = new int[10];
        foreach (char c in num) cnt[c - '0']++;
        for (int i = 0; i < num.Length; i++)
            if (cnt[i] != num[i] - '0') return false;
        return true;
    }
}
