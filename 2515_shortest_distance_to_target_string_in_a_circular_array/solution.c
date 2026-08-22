// LeetCode 2515 - Shortest Distance to Target String in a Circular Array
// https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

#include <string.h>

int closestTarget(char** words, int wordsSize, char* target, int startIndex) {
    int best = -1;
    for (int i = 0; i < wordsSize; i++) {
        if (strcmp(words[i], target) == 0) {
            int d = i - startIndex;
            if (d < 0) d = -d;
            if (wordsSize - d < d) d = wordsSize - d;
            if (best < 0 || d < best) best = d;
        }
    }
    return best;
}
