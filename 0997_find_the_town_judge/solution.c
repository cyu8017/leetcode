// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

#include <stdlib.h>

int findJudge(int n, int** trust, int trustSize, int* trustColSize) {
    (void)trustColSize;
    int* score = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < trustSize; i++) {
        score[trust[i][0]]--;
        score[trust[i][1]]++;
    }
    for (int i = 1; i <= n; i++) if (score[i] == n - 1) { free(score); return i; }
    free(score);
    return -1;
}
