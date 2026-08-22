// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** sortFeatures(char** features, int featuresSize, char** responses, int responsesSize,
                    int* returnSize) {
    int* counts = (int*)calloc((size_t)featuresSize, sizeof(int));
    int* seen = (int*)malloc((size_t)featuresSize * sizeof(int));

    for (int r = 0; r < responsesSize; r++) {
        memset(seen, 0, (size_t)featuresSize * sizeof(int));
        const char* p = responses[r];
        while (*p) {
            while (*p == ' ') {
                p++;
            }
            if (!*p) {
                break;
            }
            const char* start = p;
            while (*p && *p != ' ') {
                p++;
            }
            size_t len = (size_t)(p - start);
            for (int f = 0; f < featuresSize; f++) {
                if (!seen[f] && strlen(features[f]) == len &&
                    strncmp(features[f], start, len) == 0) {
                    seen[f] = 1;
                }
            }
        }
        for (int f = 0; f < featuresSize; f++) {
            if (seen[f]) {
                counts[f]++;
            }
        }
    }

    int* order = (int*)malloc((size_t)featuresSize * sizeof(int));
    for (int i = 0; i < featuresSize; i++) {
        order[i] = i;
    }
    for (int i = 1; i < featuresSize; i++) {
        int key = order[i];
        int j = i - 1;
        while (j >= 0 && (counts[order[j]] < counts[key] ||
                          (counts[order[j]] == counts[key] &&
                           strcmp(features[order[j]], features[key]) > 0))) {
            order[j + 1] = order[j];
            j--;
        }
        order[j + 1] = key;
    }

    char** result = (char**)malloc((size_t)featuresSize * sizeof(char*));
    for (int i = 0; i < featuresSize; i++) {
        result[i] = strdup(features[order[i]]);
    }
    *returnSize = featuresSize;

    free(counts);
    free(seen);
    free(order);
    return result;
}
