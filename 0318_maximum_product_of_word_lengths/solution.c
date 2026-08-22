// LeetCode 0318 - Maximum Product of Word Lengths
// https://leetcode.com/problems/maximum-product-of-word-lengths/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

int maxProduct(char** words, int wordsSize) {
    int* masks = (int*)malloc((size_t)wordsSize * sizeof(int));
    int* lengths = (int*)malloc((size_t)wordsSize * sizeof(int));

    for (int index = 0; index < wordsSize; index++) {
        int mask = 0;
        bool valid = true;
        for (int charIndex = 0; words[index][charIndex] != '\0'; charIndex++) {
            int bit = 1 << (words[index][charIndex] - 'a');
            if (mask & bit) {
                valid = false;
                break;
            }
            mask |= bit;
        }
        masks[index] = valid ? mask : 0;
        lengths[index] = (int)strlen(words[index]);
    }

    int best = 0;
    for (int left = 0; left < wordsSize; left++) {
        if (masks[left] == 0) {
            continue;
        }
        for (int right = left + 1; right < wordsSize; right++) {
            if (masks[right] == 0) {
                continue;
            }
            if ((masks[left] & masks[right]) == 0) {
                best = maxInt(best, lengths[left] * lengths[right]);
            }
        }
    }

    free(masks);
    free(lengths);
    return best;
}
