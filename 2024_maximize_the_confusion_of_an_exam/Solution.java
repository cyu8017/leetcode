// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        return Math.max(maxWith(answerKey, k, 'T'), maxWith(answerKey, k, 'F'));
    }

    private int maxWith(String answerKey, int k, char ch) {
        int left = 0, bad = 0, best = 0;
        for (int right = 0; right < answerKey.length(); right++) {
            if (answerKey.charAt(right) != ch) bad++;
            while (bad > k) {
                if (answerKey.charAt(left) != ch) bad--;
                left++;
            }
            best = Math.max(best, right - left + 1);
        }
        return best;
    }
}
