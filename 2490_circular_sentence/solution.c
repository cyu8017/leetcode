// LeetCode 2490 - Circular Sentence
// https://leetcode.com/problems/circular-sentence/

#include <stdbool.h>
#include <string.h>

bool isCircularSentence(char* sentence) {
    int n = (int)strlen(sentence);
    if (sentence[0] != sentence[n - 1]) return false;
    for (int i = 0; i < n; i++) {
        if (sentence[i] == ' ' && sentence[i - 1] != sentence[i + 1]) return false;
    }
    return true;
}
