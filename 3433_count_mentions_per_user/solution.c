// LeetCode 3433 - Count Mentions Per User
// https://leetcode.com/problems/count-mentions-per-user/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static int cmp_events(const void* a, const void* b) {
    char** ea = *(char*** )a; /* wrong */
    return 0;
}

/* events is char*** essentially via char** events[] - LeetCode: char*** events */
typedef struct { char** e; } Ev;

int* countMentions(int numberOfUsers, char*** events, int eventsSize, int* eventsColSize, int* returnSize) {
    (void)eventsColSize;
    /* sort by time, OFFLINE before MESSAGE */
    int* order = (int*)malloc(eventsSize * sizeof(int));
    for (int i = 0; i < eventsSize; i++) order[i] = i;
    for (int i = 0; i < eventsSize; i++) for (int j = i + 1; j < eventsSize; j++) {
        int ti = atoi(events[order[i]][1]), tj = atoi(events[order[j]][1]);
        int swap = 0;
        if (ti > tj) swap = 1;
        else if (ti == tj && strcmp(events[order[i]][0], events[order[j]][0]) < 0) swap = 1; /* MESSAGE < OFFLINE alphabetically so OFFLINE > MESSAGE -> want OFFLINE first means larger type first */
        /* Go: events[i][0] > events[j][0] means OFFLINE before MESSAGE since O > M */
        else if (ti == tj && strcmp(events[order[i]][0], events[order[j]][0]) < 0) swap = 1;
        if (ti == tj) {
            /* want OFFLINE before MESSAGE: strcmp("OFFLINE","MESSAGE")>0 so if order[i] is MESSAGE and order[j] OFFLINE, swap */
            if (strcmp(events[order[i]][0], events[order[j]][0]) < 0) swap = 1;
            else swap = 0;
            if (ti > tj) swap = 1;
            else if (ti < tj) swap = 0;
            else if (strcmp(events[order[i]][0], events[order[j]][0]) < 0) swap = 1;
            else swap = 0;
        } else swap = ti > tj;
        if (swap) { int t = order[i]; order[i] = order[j]; order[j] = t; }
    }
    bool* online = (bool*)malloc(numberOfUsers); memset(online, 1, numberOfUsers);
    int* offlineUntil = (int*)calloc(numberOfUsers, sizeof(int));
    int* ans = (int*)calloc(numberOfUsers, sizeof(int));
    for (int ei = 0; ei < eventsSize; ei++) {
        char** e = events[order[ei]];
        int t = atoi(e[1]);
        for (int i = 0; i < numberOfUsers; i++) if (!online[i] && offlineUntil[i] <= t) online[i] = true;
        if (strcmp(e[0], "OFFLINE") == 0) {
            int id = atoi(e[2]); online[id] = false; offlineUntil[id] = t + 60;
        } else {
            char* msg = e[2];
            if (strcmp(msg, "ALL") == 0) { for (int i = 0; i < numberOfUsers; i++) ans[i]++; }
            else if (strcmp(msg, "HERE") == 0) { for (int i = 0; i < numberOfUsers; i++) if (online[i]) ans[i]++; }
            else {
                char* dup = strdup(msg); char* tok = strtok(dup, " ");
                while (tok) { int id = atoi(tok + 2); ans[id]++; tok = strtok(NULL, " "); }
                free(dup);
            }
        }
    }
    free(order); free(online); free(offlineUntil);
    *returnSize = numberOfUsers;
    return ans;
}
