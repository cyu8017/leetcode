// LeetCode 0763 - Partition Labels
// https://leetcode.com/problems/partition-labels/

#include <stdlib.h>
#include <string.h>

int* partitionLabels(char* s, int* returnSize) {
    int last[26] = {0};
    int n = (int)strlen(s);
    for (int i = 0; i < n; i++) last[s[i] - 'a'] = i;
    int* answer = (int*)malloc((size_t)n * sizeof(int));
    int size = 0, start = 0, end = 0;
    for (int i = 0; i < n; i++) {
        if (last[s[i] - 'a'] > end) end = last[s[i] - 'a'];
        if (i == end) {
            answer[size++] = end - start + 1;
            start = i + 1;
        }
    }
    *returnSize = size;
    return answer;
}
