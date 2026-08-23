// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

using System;

public class Solution {
    public int MaxConsecutiveAnswers(string answerKey, int k) {
        int MaxWith(char ch) {
            int left = 0, bad = 0, best = 0;
            for (int right = 0; right < answerKey.Length; right++) {
                if (answerKey[right] != ch) bad++;
                while (bad > k) {
                    if (answerKey[left] != ch) bad--;
                    left++;
                }
                best = Math.Max(best, right - left + 1);
            }
            return best;
        }
        return Math.Max(MaxWith('T'), MaxWith('F'));
    }
}
