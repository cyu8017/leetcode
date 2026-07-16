// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int remain;
    int steps;
} State;

typedef struct {
    State* data;
    int front;
    int back;
    int capacity;
} Queue;

static void queueInit(Queue* queue) {
    queue->capacity = 64;
    queue->data = (State*)malloc((size_t)queue->capacity * sizeof(State));
    queue->front = 0;
    queue->back = 0;
}

static void queuePush(Queue* queue, State state) {
    if (queue->back >= queue->capacity) {
        queue->capacity *= 2;
        queue->data = (State*)realloc(queue->data, (size_t)queue->capacity * sizeof(State));
    }
    queue->data[queue->back++] = state;
}

static bool queueEmpty(Queue* queue) {
    return queue->front >= queue->back;
}

static State queuePop(Queue* queue) {
    return queue->data[queue->front++];
}

static void queueFree(Queue* queue) {
    free(queue->data);
}

static bool visitedContains(int* visited, int count, int value) {
    for (int i = 0; i < count; i++) {
        if (visited[i] == value) {
            return true;
        }
    }
    return false;
}

int numSquares(int n) {
    int maxSquares = 0;
    while ((maxSquares + 1) * (maxSquares + 1) <= n) {
        maxSquares++;
    }

    Queue queue;
    queueInit(&queue);
    queuePush(&queue, (State){ n, 0 });

    int* visited = (int*)malloc((size_t)(n + 2) * sizeof(int));
    int visitedCount = 0;
    visited[visitedCount++] = n;

    int result = 0;
    while (!queueEmpty(&queue)) {
        State state = queuePop(&queue);
        if (state.remain == 0) {
            result = state.steps;
            break;
        }
        for (int value = 1; value <= maxSquares; value++) {
            int square = value * value;
            int next = state.remain - square;
            if (next < 0) {
                break;
            }
            if (!visitedContains(visited, visitedCount, next)) {
                visited[visitedCount++] = next;
                queuePush(&queue, (State){ next, state.steps + 1 });
            }
        }
    }

    queueFree(&queue);
    free(visited);
    return result;
}
