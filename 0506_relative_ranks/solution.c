// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int index;
    int value;
} ScoreEntry;

static int compareScoreEntries(const void* leftPtr, const void* rightPtr) {
    const ScoreEntry* left = (const ScoreEntry*)leftPtr;
    const ScoreEntry* right = (const ScoreEntry*)rightPtr;
    return right->value - left->value;
}

static char* rankLabel(int rank) {
    if (rank == 1) {
        return strdup("Gold Medal");
    }
    if (rank == 2) {
        return strdup("Silver Medal");
    }
    if (rank == 3) {
        return strdup("Bronze Medal");
    }
    char buffer[16];
    snprintf(buffer, sizeof(buffer), "%d", rank);
    return strdup(buffer);
}

char** findRelativeRanks(int* score, int scoreSize, int* returnSize) {
    ScoreEntry* entries = (ScoreEntry*)malloc((size_t)scoreSize * sizeof(ScoreEntry));
    for (int index = 0; index < scoreSize; index++) {
        entries[index].index = index;
        entries[index].value = score[index];
    }
    qsort(entries, (size_t)scoreSize, sizeof(ScoreEntry), compareScoreEntries);

    char** result = (char**)malloc((size_t)scoreSize * sizeof(char*));
    for (int rank = 0; rank < scoreSize; rank++) {
        result[entries[rank].index] = rankLabel(rank + 1);
    }

    free(entries);
    *returnSize = scoreSize;
    return result;
}
