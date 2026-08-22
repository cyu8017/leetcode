// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

#include <stdbool.h>
#include <string.h>

bool areSentencesSimilar(char** sentence1, int sentence1Size, char** sentence2, int sentence2Size, char*** similarPairs, int similarPairsSize, int* similarPairsColSize) {
    (void)similarPairsColSize;
    if (sentence1Size != sentence2Size) {
        return false;
    }
    for (int i = 0; i < sentence1Size; i++) {
        if (strcmp(sentence1[i], sentence2[i]) == 0) {
            continue;
        }
        bool ok = false;
        for (int j = 0; j < similarPairsSize; j++) {
            if ((strcmp(sentence1[i], similarPairs[j][0]) == 0 && strcmp(sentence2[i], similarPairs[j][1]) == 0) ||
                (strcmp(sentence1[i], similarPairs[j][1]) == 0 && strcmp(sentence2[i], similarPairs[j][0]) == 0)) {
                ok = true;
                break;
            }
        }
        if (!ok) {
            return false;
        }
    }
    return true;
}
