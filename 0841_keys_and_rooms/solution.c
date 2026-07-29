// LeetCode 0841 - Keys and Rooms
// https://leetcode.com/problems/keys-and-rooms/

#include <stdbool.h>
#include <stdlib.h>

bool canVisitAllRooms(int** rooms, int roomsSize, int* roomsColSize) {
    bool* seen = (bool*)calloc((size_t)roomsSize, sizeof(bool));
    int* stack = (int*)malloc((size_t)roomsSize * sizeof(int));
    int top = 0;
    stack[top++] = 0;
    seen[0] = true;
    int visited = 1;
    while (top) {
        int room = stack[--top];
        for (int i = 0; i < roomsColSize[room]; i++) {
            int key = rooms[room][i];
            if (!seen[key]) {
                seen[key] = true;
                visited++;
                stack[top++] = key;
            }
        }
    }
    free(seen); free(stack);
    return visited == roomsSize;
}
