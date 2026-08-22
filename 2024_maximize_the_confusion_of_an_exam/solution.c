// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

#include <string.h>

static int maxWith2024(char* answerKey, int k, char ch) {
    int left = 0, bad = 0, best = 0, n = (int)strlen(answerKey);
    for (int right = 0; right < n; right++) {
        if (answerKey[right] != ch) bad++;
        while (bad > k) {
            if (answerKey[left] != ch) bad--;
            left++;
        }
        if (right - left + 1 > best) best = right - left + 1;
    }
    return best;
}

int maxConsecutiveAnswers(char* answerKey, int k) {
    int a = maxWith2024(answerKey, k, 'T');
    int b = maxWith2024(answerKey, k, 'F');
    return a > b ? a : b;
}
