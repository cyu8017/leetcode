// LeetCode 0353 - Design Snake Game
// https://leetcode.com/problems/design-snake-game/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int row;
    int col;
} Cell;

typedef struct {
    int width;
    int height;
    int** food;
    int foodSize;
    int* foodColSize;
    int foodIndex;
    int score;
    Cell* snake;
    int snakeSize;
    int snakeCapacity;
    int* bodyRows;
    int* bodyCols;
    int bodyCount;
    int bodyCapacity;
} SnakeGame;

static int bodyContains(SnakeGame* obj, int row, int col) {
    for (int index = 0; index < obj->bodyCount; index++) {
        if (obj->bodyRows[index] == row && obj->bodyCols[index] == col) {
            return 1;
        }
    }
    return 0;
}

static void bodyAdd(SnakeGame* obj, int row, int col) {
    if (obj->bodyCount >= obj->bodyCapacity) {
        int newCapacity = obj->bodyCapacity == 0 ? 4 : obj->bodyCapacity * 2;
        obj->bodyRows = (int*)realloc(obj->bodyRows, (size_t)newCapacity * sizeof(int));
        obj->bodyCols = (int*)realloc(obj->bodyCols, (size_t)newCapacity * sizeof(int));
        obj->bodyCapacity = newCapacity;
    }
    obj->bodyRows[obj->bodyCount] = row;
    obj->bodyCols[obj->bodyCount] = col;
    obj->bodyCount += 1;
}

static void bodyRemove(SnakeGame* obj, int row, int col) {
    for (int index = 0; index < obj->bodyCount; index++) {
        if (obj->bodyRows[index] == row && obj->bodyCols[index] == col) {
            obj->bodyRows[index] = obj->bodyRows[obj->bodyCount - 1];
            obj->bodyCols[index] = obj->bodyCols[obj->bodyCount - 1];
            obj->bodyCount -= 1;
            return;
        }
    }
}

SnakeGame* snakeGameCreate(int width, int height, int** food, int foodSize, int* foodColSize) {
    SnakeGame* obj = (SnakeGame*)calloc(1, sizeof(SnakeGame));
    obj->width = width;
    obj->height = height;
    obj->food = food;
    obj->foodSize = foodSize;
    obj->foodColSize = foodColSize;
    obj->snakeCapacity = 4;
    obj->snake = (Cell*)malloc((size_t)obj->snakeCapacity * sizeof(Cell));
    obj->snake[0].row = 0;
    obj->snake[0].col = 0;
    obj->snakeSize = 1;
    bodyAdd(obj, 0, 0);
    return obj;
}

int snakeGameMove(SnakeGame* obj, char* direction) {
    int row = obj->snake[0].row;
    int col = obj->snake[0].col;

    if (strcmp(direction, "U") == 0) {
        row -= 1;
    } else if (strcmp(direction, "D") == 0) {
        row += 1;
    } else if (strcmp(direction, "L") == 0) {
        col -= 1;
    } else {
        col += 1;
    }

    if (row < 0 || row >= obj->height || col < 0 || col >= obj->width) {
        return -1;
    }

    int willEat = obj->foodIndex < obj->foodSize
        && row == obj->food[obj->foodIndex][0]
        && col == obj->food[obj->foodIndex][1];

    if (!willEat) {
        Cell tail = obj->snake[obj->snakeSize - 1];
        obj->snakeSize -= 1;
        bodyRemove(obj, tail.row, tail.col);
    }

    if (bodyContains(obj, row, col)) {
        return -1;
    }

    if (obj->snakeSize >= obj->snakeCapacity) {
        obj->snakeCapacity *= 2;
        obj->snake = (Cell*)realloc(obj->snake, (size_t)obj->snakeCapacity * sizeof(Cell));
    }

    for (int index = obj->snakeSize; index > 0; index--) {
        obj->snake[index] = obj->snake[index - 1];
    }
    obj->snake[0].row = row;
    obj->snake[0].col = col;
    obj->snakeSize += 1;
    bodyAdd(obj, row, col);

    if (willEat) {
        obj->score += 1;
        obj->foodIndex += 1;
    }

    return obj->score;
}

void snakeGameFree(SnakeGame* obj) {
    free(obj->snake);
    free(obj->bodyRows);
    free(obj->bodyCols);
    free(obj);
}
