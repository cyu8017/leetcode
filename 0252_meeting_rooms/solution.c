// LeetCode 0252 - Meeting Rooms
// https://leetcode.com/problems/meeting-rooms/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int start;
    int end;
} Interval;

static int cmpInterval(const void* left, const void* right) {
    return ((const Interval*)left)->start - ((const Interval*)right)->start;
}

bool canAttendMeetings(int** intervals, int intervalsSize, int* intervalsColSize) {
    Interval* sorted = (Interval*)malloc((size_t)intervalsSize * sizeof(Interval));
    for (int i = 0; i < intervalsSize; i++) {
        sorted[i].start = intervals[i][0];
        sorted[i].end = intervals[i][1];
    }
    qsort(sorted, (size_t)intervalsSize, sizeof(Interval), cmpInterval);

    for (int index = 1; index < intervalsSize; index++) {
        if (sorted[index].start < sorted[index - 1].end) {
            free(sorted);
            return false;
        }
    }

    free(sorted);
    return true;
}
