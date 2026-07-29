// LeetCode 1462 - Course Schedule IV
// https://leetcode.com/problems/course-schedule-iv/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool* checkIfPrerequisite(int numCourses, int** prerequisites, int prerequisitesSize, int* prerequisitesColSize,
                          int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)prerequisitesColSize; (void)queriesColSize;
    bool* reach = (bool*)calloc(numCourses * numCourses, sizeof(bool));
    for (int i = 0; i < prerequisitesSize; i++)
        reach[prerequisites[i][0] * numCourses + prerequisites[i][1]] = true;
    for (int k = 0; k < numCourses; k++)
        for (int i = 0; i < numCourses; i++)
            if (reach[i * numCourses + k])
                for (int j = 0; j < numCourses; j++)
                    reach[i * numCourses + j] |= reach[k * numCourses + j];
    bool* ans = (bool*)malloc(queriesSize * sizeof(bool));
    for (int i = 0; i < queriesSize; i++)
        ans[i] = reach[queries[i][0] * numCourses + queries[i][1]];
    free(reach);
    *returnSize = queriesSize;
    return ans;
}
