// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct {
    char* tag;
} Tag;

typedef struct {
    int id;
    char* description;
    int dueDate;
    char** tags;
    int tagsSize;
    bool done;
    int userId;
} Task;

typedef struct {
    int* ids;
    int size;
    int cap;
} UserTasks;

typedef struct {
    int nextID;
    Task** tasks;
    int tasksCap;
    UserTasks* users;
    int usersCap;
} TodoList;

TodoList* todoListCreate(void) {
    TodoList* t = (TodoList*)calloc(1, sizeof(TodoList));
    t->nextID = 1;
    t->tasksCap = 1024;
    t->tasks = (Task**)calloc((size_t)t->tasksCap, sizeof(Task*));
    t->usersCap = 1024;
    t->users = (UserTasks*)calloc((size_t)t->usersCap, sizeof(UserTasks));
    return t;
}

static void ensureUser(TodoList* obj, int userId) {
    if (userId >= obj->usersCap) {
        int nc = userId * 2 + 16;
        obj->users = (UserTasks*)realloc(obj->users, (size_t)nc * sizeof(UserTasks));
        for (int i = obj->usersCap; i < nc; i++) {
            obj->users[i].ids = NULL;
            obj->users[i].size = 0;
            obj->users[i].cap = 0;
        }
        obj->usersCap = nc;
    }
}

int todoListAddTask(TodoList* obj, int userId, char* taskDescription, int dueDate, char** tags, int tagsSize) {
    int id = obj->nextID++;
    if (id >= obj->tasksCap) {
        int nc = obj->tasksCap * 2;
        obj->tasks = (Task**)realloc(obj->tasks, (size_t)nc * sizeof(Task*));
        for (int i = obj->tasksCap; i < nc; i++) obj->tasks[i] = NULL;
        obj->tasksCap = nc;
    }
    Task* tk = (Task*)calloc(1, sizeof(Task));
    tk->id = id;
    tk->description = (char*)malloc(strlen(taskDescription) + 1);
    strcpy(tk->description, taskDescription);
    tk->dueDate = dueDate;
    tk->tagsSize = tagsSize;
    tk->tags = (char**)malloc((size_t)tagsSize * sizeof(char*));
    for (int i = 0; i < tagsSize; i++) {
        tk->tags[i] = (char*)malloc(strlen(tags[i]) + 1);
        strcpy(tk->tags[i], tags[i]);
    }
    tk->userId = userId;
    obj->tasks[id] = tk;
    ensureUser(obj, userId);
    UserTasks* u = &obj->users[userId];
    if (u->size == u->cap) {
        u->cap = u->cap ? u->cap * 2 : 8;
        u->ids = (int*)realloc(u->ids, (size_t)u->cap * sizeof(int));
    }
    u->ids[u->size++] = id;
    return id;
}

typedef struct { TodoList* obj; int* ids; } SortCtx;
static SortCtx gctx;
static int cmpDueG(const void* a, const void* b) {
    int ia = *(const int*)a, ib = *(const int*)b;
    return gctx.obj->tasks[ia]->dueDate - gctx.obj->tasks[ib]->dueDate;
}

char** todoListGetAllTasks(TodoList* obj, int userId, int* retSize) {
    if (userId >= obj->usersCap) { *retSize = 0; return NULL; }
    UserTasks* u = &obj->users[userId];
    int* ids = (int*)malloc((size_t)u->size * sizeof(int));
    for (int i = 0; i < u->size; i++) ids[i] = u->ids[i];
    gctx.obj = obj;
    qsort(ids, (size_t)u->size, sizeof(int), cmpDueG);
    char** ans = (char**)malloc((size_t)u->size * sizeof(char*));
    int ac = 0;
    for (int i = 0; i < u->size; i++) {
        Task* tk = obj->tasks[ids[i]];
        if (!tk->done) {
            ans[ac] = (char*)malloc(strlen(tk->description) + 1);
            strcpy(ans[ac], tk->description);
            ac++;
        }
    }
    free(ids);
    *retSize = ac;
    return ans;
}

char** todoListGetTasksForTag(TodoList* obj, int userId, char* tag, int* retSize) {
    if (userId >= obj->usersCap) { *retSize = 0; return NULL; }
    UserTasks* u = &obj->users[userId];
    int* ids = (int*)malloc((size_t)u->size * sizeof(int));
    for (int i = 0; i < u->size; i++) ids[i] = u->ids[i];
    gctx.obj = obj;
    qsort(ids, (size_t)u->size, sizeof(int), cmpDueG);
    char** ans = (char**)malloc((size_t)u->size * sizeof(char*));
    int ac = 0;
    for (int i = 0; i < u->size; i++) {
        Task* tk = obj->tasks[ids[i]];
        if (tk->done) continue;
        bool has = false;
        for (int j = 0; j < tk->tagsSize; j++) {
            if (strcmp(tk->tags[j], tag) == 0) { has = true; break; }
        }
        if (has) {
            ans[ac] = (char*)malloc(strlen(tk->description) + 1);
            strcpy(ans[ac], tk->description);
            ac++;
        }
    }
    free(ids);
    *retSize = ac;
    return ans;
}

void todoListCompleteTask(TodoList* obj, int userId, int taskId) {
    if (taskId <= 0 || taskId >= obj->tasksCap || !obj->tasks[taskId]) return;
    Task* tk = obj->tasks[taskId];
    if (tk->userId != userId || tk->done) return;
    tk->done = true;
}

void todoListFree(TodoList* obj) {
    if (!obj) return;
    for (int i = 0; i < obj->tasksCap; i++) {
        Task* tk = obj->tasks[i];
        if (!tk) continue;
        free(tk->description);
        for (int j = 0; j < tk->tagsSize; j++) free(tk->tags[j]);
        free(tk->tags);
        free(tk);
    }
    free(obj->tasks);
    for (int i = 0; i < obj->usersCap; i++) free(obj->users[i].ids);
    free(obj->users);
    free(obj);
}
