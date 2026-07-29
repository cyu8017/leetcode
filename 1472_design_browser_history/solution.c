// LeetCode 1472 - Design Browser History
// https://leetcode.com/problems/design-browser-history/

#include <stdlib.h>
#include <string.h>

typedef struct {
    char** history;
    int size;
    int cap;
    int index;
} BrowserHistory;

BrowserHistory* browserHistoryCreate(char* homepage) {
    BrowserHistory* obj = (BrowserHistory*)malloc(sizeof(BrowserHistory));
    obj->cap = 16; obj->size = 1; obj->index = 0;
    obj->history = (char**)malloc(obj->cap * sizeof(char*));
    obj->history[0] = (char*)malloc(strlen(homepage) + 1);
    strcpy(obj->history[0], homepage);
    return obj;
}

void browserHistoryVisit(BrowserHistory* obj, char* url) {
    for (int i = obj->index + 1; i < obj->size; i++) free(obj->history[i]);
    obj->size = obj->index + 1;
    if (obj->size == obj->cap) {
        obj->cap *= 2;
        obj->history = (char**)realloc(obj->history, obj->cap * sizeof(char*));
    }
    obj->history[obj->size] = (char*)malloc(strlen(url) + 1);
    strcpy(obj->history[obj->size], url);
    obj->index = obj->size++;
}

char* browserHistoryBack(BrowserHistory* obj, int steps) {
    obj->index -= steps;
    if (obj->index < 0) obj->index = 0;
    return obj->history[obj->index];
}

char* browserHistoryForward(BrowserHistory* obj, int steps) {
    obj->index += steps;
    if (obj->index >= obj->size) obj->index = obj->size - 1;
    return obj->history[obj->index];
}

void browserHistoryFree(BrowserHistory* obj) {
    for (int i = 0; i < obj->size; i++) free(obj->history[i]);
    free(obj->history); free(obj);
}
