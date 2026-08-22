// LeetCode 0245 - Shortest Word Distance III
// https://leetcode.com/problems/shortest-word-distance-iii/

#include <limits.h>
#include <string.h>

int shortestWordDistance(char** wordsDict, int wordsDictSize, char* word1, char* word2) {
    if (strcmp(word1, word2) == 0) {
        int previous = -1;
        int best = INT_MAX;
        for (int index = 0; index < wordsDictSize; ++index) {
            if (strcmp(wordsDict[index], word1) == 0) {
                if (previous >= 0) {
                    int distance = index - previous;
                    if (distance < best) {
                        best = distance;
                    }
                }
                previous = index;
            }
        }
        return best;
    }

    int index1 = -1;
    int index2 = -1;
    int best = INT_MAX;
    for (int index = 0; index < wordsDictSize; ++index) {
        char* word = wordsDict[index];
        if (strcmp(word, word1) == 0) {
            index1 = index;
            if (index2 >= 0) {
                int distance = index - index2;
                if (distance < best) {
                    best = distance;
                }
            }
        }
        if (strcmp(word, word2) == 0) {
            index2 = index;
            if (index1 >= 0) {
                int distance = index - index1;
                if (distance < best) {
                    best = distance;
                }
            }
        }
    }
    return best;
}
