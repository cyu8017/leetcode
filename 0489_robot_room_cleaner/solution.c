// LeetCode 0489 - Robot Room Cleaner
// https://leetcode.com/problems/robot-room-cleaner/

#include <stdbool.h>
#include <stdlib.h>

typedef struct Robot Robot;

struct Robot {
    bool (*move)(Robot* robot);
    void (*turnLeft)(Robot* robot);
    void (*turnRight)(Robot* robot);
    void (*clean)(Robot* robot);
};

typedef struct {
    int row;
    int col;
    int direction;
} VisitState;

static bool visitContains(VisitState* visited, int size, int row, int col, int direction) {
    for (int index = 0; index < size; index++) {
        if (visited[index].row == row && visited[index].col == col &&
            visited[index].direction == direction) {
            return true;
        }
    }
    return false;
}

static void visitAdd(VisitState** visited, int* size, int* capacity, int row, int col, int direction) {
    if (*size >= *capacity) {
        *capacity *= 2;
        *visited = (VisitState*)realloc(*visited, (size_t)(*capacity) * sizeof(VisitState));
    }
    (*visited)[*size].row = row;
    (*visited)[*size].col = col;
    (*visited)[(*size)++].direction = direction;
}

static void backtrack(
    Robot* robot,
    int row,
    int col,
    int direction,
    VisitState** visited,
    int* visitSize,
    int* visitCapacity) {
    const int directions[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    robot->clean(robot);
    for (int step = 0; step < 4; step++) {
        int nextDirection = (direction + step) % 4;
        int nextRow = row + directions[nextDirection][0];
        int nextCol = col + directions[nextDirection][1];
        if (!visitContains(*visited, *visitSize, nextRow, nextCol, nextDirection) && robot->move(robot)) {
            visitAdd(visited, visitSize, visitCapacity, nextRow, nextCol, nextDirection);
            backtrack(robot, nextRow, nextCol, nextDirection, visited, visitSize, visitCapacity);
            robot->turnRight(robot);
            robot->turnRight(robot);
            robot->move(robot);
            robot->turnRight(robot);
            robot->turnRight(robot);
        }
        robot->turnRight(robot);
    }
}

void cleanRoom(Robot* robot) {
    VisitState* visited = NULL;
    int visitSize = 0;
    int visitCapacity = 0;
    visitAdd(&visited, &visitSize, &visitCapacity, 0, 0, 0);
    backtrack(robot, 0, 0, 0, &visited, &visitSize, &visitCapacity);
    free(visited);
}
