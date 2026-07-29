// LeetCode 0855 - Exam Room
// https://leetcode.com/problems/exam-room/

#include <stdlib.h>

typedef struct {
    int n;
    int* seats;
    int size;
    int cap;
} ExamRoom;

ExamRoom* examRoomCreate(int n) {
    ExamRoom* obj = (ExamRoom*)malloc(sizeof(ExamRoom));
    obj->n = n;
    obj->size = 0;
    obj->cap = 16;
    obj->seats = (int*)malloc((size_t)obj->cap * sizeof(int));
    return obj;
}

int examRoomSeat(ExamRoom* obj) {
    if (obj->size == 0) {
        obj->seats[obj->size++] = 0;
        return 0;
    }
    int best_seat = 0;
    int best_dist = obj->seats[0];
    for (int i = 1; i < obj->size; i++) {
        int dist = (obj->seats[i] - obj->seats[i - 1]) / 2;
        if (dist > best_dist) {
            best_dist = dist;
            best_seat = obj->seats[i - 1] + dist;
        }
    }
    if (obj->n - 1 - obj->seats[obj->size - 1] > best_dist)
        best_seat = obj->n - 1;
    if (obj->size == obj->cap) {
        obj->cap *= 2;
        obj->seats = (int*)realloc(obj->seats, (size_t)obj->cap * sizeof(int));
    }
    int i = obj->size;
    while (i > 0 && obj->seats[i - 1] > best_seat) {
        obj->seats[i] = obj->seats[i - 1];
        i--;
    }
    obj->seats[i] = best_seat;
    obj->size++;
    return best_seat;
}

void examRoomLeave(ExamRoom* obj, int p) {
    int i = 0;
    while (i < obj->size && obj->seats[i] != p) i++;
    if (i < obj->size) {
        for (int j = i; j < obj->size - 1; j++) obj->seats[j] = obj->seats[j + 1];
        obj->size--;
    }
}

void examRoomFree(ExamRoom* obj) {
    free(obj->seats);
    free(obj);
}
