// LeetCode 2365 - Task Scheduler II
// https://leetcode.com/problems/task-scheduler-ii/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int key; long long val; bool used; } Ent;

long long taskSchedulerII(int* tasks, int tasksSize, int space) {
    int cap = 1;
    while (cap < tasksSize * 2 + 8) cap <<= 1;
    Ent* next = (Ent*)calloc((size_t)cap, sizeof(Ent));
    long long day = 0;
    for (int i = 0; i < tasksSize; i++) {
        int t = tasks[i];
        unsigned h = (unsigned)t * 2654435761u;
        int j = (int)(h & (unsigned)(cap - 1));
        while (next[j].used && next[j].key != t) j = (j + 1) & (cap - 1);
        if (next[j].used && next[j].val > day) day = next[j].val;
        day++;
        if (!next[j].used) { next[j].used = true; next[j].key = t; }
        next[j].val = day + space;
    }
    free(next);
    return day;
}
