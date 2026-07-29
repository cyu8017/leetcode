// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int* starts;
    int* ends;
    int size;
    int capacity;
} MyCalendar;

MyCalendar* myCalendarCreate(void) {
    return (MyCalendar*)calloc(1, sizeof(MyCalendar));
}

bool myCalendarBook(MyCalendar* obj, int startTime, int endTime) {
    for (int i = 0; i < obj->size; i++) {
        if (obj->starts[i] < endTime && startTime < obj->ends[i]) {
            return false;
        }
    }
    if (obj->size == obj->capacity) {
        obj->capacity = obj->capacity ? obj->capacity * 2 : 8;
        obj->starts = (int*)realloc(obj->starts, (size_t)obj->capacity * sizeof(int));
        obj->ends = (int*)realloc(obj->ends, (size_t)obj->capacity * sizeof(int));
    }
    obj->starts[obj->size] = startTime;
    obj->ends[obj->size] = endTime;
    obj->size++;
    return true;
}

void myCalendarFree(MyCalendar* obj) {
    free(obj->starts);
    free(obj->ends);
    free(obj);
}
