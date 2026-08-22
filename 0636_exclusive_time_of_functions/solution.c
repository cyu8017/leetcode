// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

#include <stdlib.h>
#include <string.h>

int* exclusiveTime(int n, char** logs, int logsSize, int* returnSize) {
    int* result = (int*)calloc((size_t)n, sizeof(int));
    int* stack = (int*)malloc((size_t)logsSize * sizeof(int));
    int top = 0;
    int prevTime = 0;
    for (int i = 0; i < logsSize; i++) {
        char buf[64];
        strncpy(buf, logs[i], sizeof(buf) - 1);
        buf[sizeof(buf) - 1] = '\0';
        char* idStr = strtok(buf, ":");
        char* event = strtok(NULL, ":");
        char* timeStr = strtok(NULL, ":");
        int funcId = atoi(idStr);
        int time = atoi(timeStr);
        if (strcmp(event, "start") == 0) {
            if (top > 0) {
                result[stack[top - 1]] += time - prevTime;
            }
            stack[top++] = funcId;
            prevTime = time;
        } else {
            result[stack[--top]] += time - prevTime + 1;
            prevTime = time + 1;
        }
    }
    free(stack);
    *returnSize = n;
    return result;
}
