// LeetCode 2446 - Determine if Two Events Have Conflict
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

#include <stdbool.h>
#include <string.h>

bool haveConflict(char** event1, int event1Size, char** event2, int event2Size) {
    (void)event1Size;
    (void)event2Size;
    return strcmp(event1[0], event2[1]) <= 0 && strcmp(event2[0], event1[1]) <= 0;
}
