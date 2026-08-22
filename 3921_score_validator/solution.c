// LeetCode 3921 - Score Validator
// https://leetcode.com/problems/score-validator/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int* scoreValidator(char** events, int eventsSize, int* returnSize) {
    int score = 0, counter = 0;
    for (int i = 0; i < eventsSize; i++) {
        char* event = events[i];
        char* end = NULL;
        long num = strtol(event, &end, 10);
        if (end != event && *end == '\0') {
            score += (int)num;
        } else if (strcmp(event, "W") == 0) {
            counter++;
            if (counter == 10) break;
        } else {
            score++;
        }
    }
    int* ans = malloc(2 * sizeof(int));
    ans[0] = score;
    ans[1] = counter;
    *returnSize = 2;
    return ans;
}
