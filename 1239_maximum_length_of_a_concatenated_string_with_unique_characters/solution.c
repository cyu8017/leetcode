// LeetCode 1239 - Maximum Length of a Concatenated String with Unique Characters
// https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

#include <stdlib.h>
#include <string.h>

int maxLength(char** arr, int arrSize) {
    int* masks = (int*)malloc(1024 * sizeof(int));
    int* lengths = (int*)malloc(1024 * sizeof(int));
    int count = 1;
    masks[0] = 0;
    lengths[0] = 0;
    for (int w = 0; w < arrSize; w++) {
        int mask = 0;
        int valid = 1;
        for (int i = 0; arr[w][i]; i++) {
            int bit = 1 << (arr[w][i] - 'a');
            if (mask & bit) {
                valid = 0;
                break;
            }
            mask |= bit;
        }
        if (!valid) continue;
        int wordLen = (int)strlen(arr[w]);
        int oldCount = count;
        for (int i = 0; i < oldCount; i++) {
            if (masks[i] & mask) continue;
            masks[count] = masks[i] | mask;
            lengths[count] = lengths[i] + wordLen;
            count++;
        }
    }
    int ans = 0;
    for (int i = 0; i < count; i++) {
        if (lengths[i] > ans) ans = lengths[i];
    }
    free(masks);
    free(lengths);
    return ans;
}
