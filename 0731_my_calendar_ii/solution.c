// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* bStarts;
    int* bEnds;
    int bSize;
    int bCap;
    int* oStarts;
    int* oEnds;
    int oSize;
    int oCap;
} MyCalendarTwo;

MyCalendarTwo* myCalendarTwoCreate(void) {
    return (MyCalendarTwo*)calloc(1, sizeof(MyCalendarTwo));
}

bool myCalendarTwoBook(MyCalendarTwo* obj, int startTime, int endTime) {
    for (int i = 0; i < obj->oSize; i++) {
        if (obj->oStarts[i] < endTime && startTime < obj->oEnds[i]) {
            return false;
        }
    }
    for (int i = 0; i < obj->bSize; i++) {
        if (obj->bStarts[i] < endTime && startTime < obj->bEnds[i]) {
            if (obj->oSize == obj->oCap) {
                obj->oCap = obj->oCap ? obj->oCap * 2 : 8;
                obj->oStarts = (int*)realloc(obj->oStarts, (size_t)obj->oCap * sizeof(int));
                obj->oEnds = (int*)realloc(obj->oEnds, (size_t)obj->oCap * sizeof(int));
            }
            int s = obj->bStarts[i] > startTime ? obj->bStarts[i] : startTime;
            int e = obj->bEnds[i] < endTime ? obj->bEnds[i] : endTime;
            obj->oStarts[obj->oSize] = s;
            obj->oEnds[obj->oSize] = e;
            obj->oSize++;
        }
    }
    if (obj->bSize == obj->bCap) {
        obj->bCap = obj->bCap ? obj->bCap * 2 : 8;
        obj->bStarts = (int*)realloc(obj->bStarts, (size_t)obj->bCap * sizeof(int));
        obj->bEnds = (int*)realloc(obj->bEnds, (size_t)obj->bCap * sizeof(int));
    }
    obj->bStarts[obj->bSize] = startTime;
    obj->bEnds[obj->bSize] = endTime;
    obj->bSize++;
    return true;
}

void myCalendarTwoFree(MyCalendarTwo* obj) {
    free(obj->bStarts);
    free(obj->bEnds);
    free(obj->oStarts);
    free(obj->oEnds);
    free(obj);
}
