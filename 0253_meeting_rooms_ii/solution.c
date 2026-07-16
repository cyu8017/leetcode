// LeetCode 0253 - Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii/

#include <stdlib.h>

static int cmpInt(const void* left, const void* right) {
    return *(const int*)left - *(const int*)right;
}

int minMeetingRooms(int** intervals, int intervalsSize, int* intervalsColSize) {
    int* starts = (int*)malloc((size_t)intervalsSize * sizeof(int));
    int* ends = (int*)malloc((size_t)intervalsSize * sizeof(int));
    for (int index = 0; index < intervalsSize; index++) {
        starts[index] = intervals[index][0];
        ends[index] = intervals[index][1];
    }
    qsort(starts, (size_t)intervalsSize, sizeof(int), cmpInt);
    qsort(ends, (size_t)intervalsSize, sizeof(int), cmpInt);

    int rooms = 0;
    int maxRooms = 0;
    int startIndex = 0;
    int endIndex = 0;
    while (startIndex < intervalsSize) {
        if (starts[startIndex] < ends[endIndex]) {
            rooms += 1;
            if (rooms > maxRooms) {
                maxRooms = rooms;
            }
            startIndex += 1;
        } else {
            rooms -= 1;
            endIndex += 1;
        }
    }

    free(starts);
    free(ends);
    return maxRooms;
}
