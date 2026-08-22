// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

#include <stdbool.h>
#include <string.h>

bool uniqueOccurrences(int* arr, int arrSize) {
    int freq[2001];
    memset(freq, 0, sizeof(freq));
    for (int i = 0; i < arrSize; i++) freq[arr[i] + 1000]++;
    int seen[arrSize];
    int seenCount = 0;
    for (int i = 0; i <= 2000; i++) {
        if (freq[i] == 0) continue;
        for (int j = 0; j < seenCount; j++) {
            if (seen[j] == freq[i]) return false;
        }
        seen[seenCount++] = freq[i];
    }
    return true;
}
