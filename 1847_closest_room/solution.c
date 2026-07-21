// LeetCode 1847 - Closest Room
// https://leetcode.com/problems/closest-room/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    int size;
} Room;

typedef struct {
    int preferred;
    int minSize;
    int index;
} Query;

static int cmpRoomSize(const void* a, const void* b) {
    const Room* x = (const Room*)a;
    const Room* y = (const Room*)b;
    return (x->size > y->size) - (x->size < y->size);
}

static int cmpQuerySizeDesc(const void* a, const void* b) {
    const Query* x = (const Query*)a;
    const Query* y = (const Query*)b;
    return (y->minSize > x->minSize) - (y->minSize < x->minSize);
}

static int lowerBound(int* arr, int n, int target) {
    int lo = 0, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return lo;
}

static void insertSorted(int* arr, int* n, int value) {
    int pos = lowerBound(arr, *n, value);
    memmove(arr + pos + 1, arr + pos, (size_t)(*n - pos) * sizeof(int));
    arr[pos] = value;
    (*n)++;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestRoom(int** rooms, int roomsSize, int* roomsColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)roomsColSize;
    (void)queriesColSize;
    Room* roomArr = (Room*)malloc((size_t)roomsSize * sizeof(Room));
    for (int i = 0; i < roomsSize; i++) {
        roomArr[i].id = rooms[i][0];
        roomArr[i].size = rooms[i][1];
    }
    qsort(roomArr, (size_t)roomsSize, sizeof(Room), cmpRoomSize);

    Query* queryArr = (Query*)malloc((size_t)queriesSize * sizeof(Query));
    for (int i = 0; i < queriesSize; i++) {
        queryArr[i].preferred = queries[i][0];
        queryArr[i].minSize = queries[i][1];
        queryArr[i].index = i;
    }
    qsort(queryArr, (size_t)queriesSize, sizeof(Query), cmpQuerySizeDesc);

    int* available = (int*)malloc((size_t)roomsSize * sizeof(int));
    int availableSize = 0;
    int roomIndex = roomsSize - 1;
    int* answer = (int*)malloc((size_t)queriesSize * sizeof(int));
    for (int i = 0; i < queriesSize; i++) answer[i] = -1;

    for (int qi = 0; qi < queriesSize; qi++) {
        int preferred = queryArr[qi].preferred;
        int minSize = queryArr[qi].minSize;
        while (roomIndex >= 0 && roomArr[roomIndex].size >= minSize) {
            insertSorted(available, &availableSize, roomArr[roomIndex].id);
            roomIndex--;
        }
        if (!availableSize) continue;

        int pos = lowerBound(available, availableSize, preferred);
        int bestId = -1;
        int bestDist = 2147483647;

        if (pos < availableSize) {
            int roomId = available[pos];
            int dist = roomId >= preferred ? roomId - preferred : preferred - roomId;
            if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
                bestId = roomId;
                bestDist = dist;
            }
        }
        if (pos > 0) {
            int roomId = available[pos - 1];
            int dist = roomId >= preferred ? roomId - preferred : preferred - roomId;
            if (dist < bestDist || (dist == bestDist && roomId < bestId)) {
                bestId = roomId;
                bestDist = dist;
            }
        }
        answer[queryArr[qi].index] = bestId;
    }

    free(available);
    free(queryArr);
    free(roomArr);
    *returnSize = queriesSize;
    return answer;
}
