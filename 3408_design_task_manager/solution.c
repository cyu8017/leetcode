// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

#include <stdlib.h>
#include <string.h>

typedef struct { int pri, taskId, userId; } TaskItem;
typedef struct {
    TaskItem* h; int hn, hcap;
    int* pri; int* user; char* has;
} TaskManager;

#define MAX_TID 100010

static void heap_up(TaskItem* h, int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        int better = h[i].pri > h[p].pri || (h[i].pri == h[p].pri && h[i].taskId > h[p].taskId);
        if (!better) break;
        TaskItem t = h[p]; h[p] = h[i]; h[i] = t; i = p;
    }
}
static void heap_down(TaskItem* h, int n, int i) {
    for (;;) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < n && (h[l].pri > h[s].pri || (h[l].pri == h[s].pri && h[l].taskId > h[s].taskId))) s = l;
        if (r < n && (h[r].pri > h[s].pri || (h[r].pri == h[s].pri && h[r].taskId > h[s].taskId))) s = r;
        if (s == i) break;
        TaskItem t = h[s]; h[s] = h[i]; h[i] = t; i = s;
    }
}
static void tm_push(TaskManager* obj, int pri, int taskId, int userId) {
    if (obj->hn == obj->hcap) { obj->hcap *= 2; obj->h = (TaskItem*)realloc(obj->h, obj->hcap * sizeof(TaskItem)); }
    obj->h[obj->hn] = (TaskItem){pri, taskId, userId}; heap_up(obj->h, obj->hn); obj->hn++;
}

TaskManager* taskManagerCreate(int** tasks, int tasksSize, int* tasksColSize) {
    (void)tasksColSize;
    TaskManager* tm = (TaskManager*)calloc(1, sizeof(TaskManager));
    tm->hcap = 16; tm->h = (TaskItem*)malloc(tm->hcap * sizeof(TaskItem));
    tm->pri = (int*)calloc(MAX_TID, sizeof(int));
    tm->user = (int*)calloc(MAX_TID, sizeof(int));
    tm->has = (char*)calloc(MAX_TID, 1);
    for (int i = 0; i < tasksSize; i++) {
        int userId = tasks[i][0], taskId = tasks[i][1], priority = tasks[i][2];
        tm->pri[taskId] = priority; tm->user[taskId] = userId; tm->has[taskId] = 1;
        tm_push(tm, priority, taskId, userId);
    }
    return tm;
}

void taskManagerAdd(TaskManager* obj, int userId, int taskId, int priority) {
    obj->pri[taskId] = priority; obj->user[taskId] = userId; obj->has[taskId] = 1;
    tm_push(obj, priority, taskId, userId);
}

void taskManagerEdit(TaskManager* obj, int taskId, int newPriority) {
    obj->pri[taskId] = newPriority;
    tm_push(obj, newPriority, taskId, obj->user[taskId]);
}

void taskManagerRmv(TaskManager* obj, int taskId) { obj->has[taskId] = 0; }

int taskManagerExecTop(TaskManager* obj) {
    while (obj->hn > 0) {
        TaskItem top = obj->h[0];
        obj->h[0] = obj->h[--obj->hn];
        if (obj->hn) heap_down(obj->h, obj->hn, 0);
        if (obj->has[top.taskId] && obj->pri[top.taskId] == top.pri && obj->user[top.taskId] == top.userId) {
            obj->has[top.taskId] = 0;
            return top.userId;
        }
    }
    return -1;
}

void taskManagerFree(TaskManager* obj) {
    free(obj->h); free(obj->pri); free(obj->user); free(obj->has); free(obj);
}
