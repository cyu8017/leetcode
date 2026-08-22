// LeetCode 0187 - Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/

#include <stdlib.h>
#include <string.h>

char** findRepeatedDnaSequences(char* s, int* returnSize) {
    int length = strlen(s);
    int capacity = length > 9 ? length - 9 : 1;
    char** result = malloc(capacity * sizeof(*result));
    char** seen = malloc(capacity * sizeof(*seen));
    int seenSize = 0;
    *returnSize = 0;

    for (int i = 0; i + 10 <= length; ++i) {
        char sequence[11];
        memcpy(sequence, s + i, 10);
        sequence[10] = '\0';

        int index = 0;
        while (index < seenSize && strcmp(seen[index], sequence) != 0) {
            ++index;
        }
        if (index == seenSize) {
            seen[seenSize] = malloc(11);
            strcpy(seen[seenSize++], sequence);
        } else {
            int alreadyRepeated = 0;
            for (int j = 0; j < *returnSize; ++j) {
                if (strcmp(result[j], sequence) == 0) {
                    alreadyRepeated = 1;
                    break;
                }
            }
            if (!alreadyRepeated) {
                result[*returnSize] = malloc(11);
                strcpy(result[(*returnSize)++], sequence);
            }
        }
    }

    for (int i = 0; i < seenSize; ++i) {
        free(seen[i]);
    }
    free(seen);
    return result;
}