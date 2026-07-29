// LeetCode 1125 - Smallest Sufficient Team
// https://leetcode.com/problems/smallest-sufficient-team/

#include <stdlib.h>
#include <string.h>

int* smallestSufficientTeam(char** req_skills, int req_skillsSize, char*** people, int peopleSize, int* peopleColSize, int* returnSize) {
    int* personMasks = (int*)calloc((size_t)peopleSize, sizeof(int));
    for (int i = 0; i < peopleSize; i++) {
        for (int j = 0; j < peopleColSize[i]; j++) {
            for (int s = 0; s < req_skillsSize; s++) {
                if (strcmp(people[i][j], req_skills[s]) == 0) {
                    personMasks[i] |= 1 << s;
                    break;
                }
            }
        }
    }
    int target = (1 << req_skillsSize) - 1;
    int states = target + 1;
    int* dpLen = (int*)malloc((size_t)states * sizeof(int));
    long long* dpMask = (long long*)malloc((size_t)states * sizeof(long long));
    for (int i = 0; i < states; i++) {
        dpLen[i] = peopleSize + 1;
        dpMask[i] = 0;
    }
    dpLen[0] = 0;
    for (int state = 0; state < states; state++) {
        if (dpLen[state] > peopleSize) continue;
        for (int i = 0; i < peopleSize; i++) {
            int next = state | personMasks[i];
            if (dpLen[state] + 1 < dpLen[next]) {
                dpLen[next] = dpLen[state] + 1;
                dpMask[next] = dpMask[state] | (1LL << i);
            }
        }
    }
    long long chosen = dpMask[target];
    int* ans = (int*)malloc((size_t)dpLen[target] * sizeof(int));
    int idx = 0;
    for (int i = 0; i < peopleSize; i++) {
        if (chosen & (1LL << i)) ans[idx++] = i;
    }
    *returnSize = idx;
    free(personMasks);
    free(dpLen);
    free(dpMask);
    return ans;
}
