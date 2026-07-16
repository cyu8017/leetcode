// LeetCode 0305 - Number of Islands II
// https://leetcode.com/problems/number-of-islands-ii/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int index;
    int parent;
    int rank;
} Node;

typedef struct {
    Node* nodes;
    int size;
    int capacity;
} UnionFind;

static int findNode(UnionFind* uf, int index) {
    for (int position = 0; position < uf->size; position++) {
        if (uf->nodes[position].index == index) {
            if (uf->nodes[position].parent != index) {
                uf->nodes[position].parent = findNode(uf, uf->nodes[position].parent);
            }
            return uf->nodes[position].parent;
        }
    }
    return -1;
}

static int addNode(UnionFind* uf, int index) {
    for (int position = 0; position < uf->size; position++) {
        if (uf->nodes[position].index == index) {
            return position;
        }
    }
    if (uf->size == uf->capacity) {
        uf->capacity = uf->capacity ? uf->capacity * 2 : 8;
        uf->nodes = realloc(uf->nodes, (size_t)uf->capacity * sizeof(Node));
    }
    uf->nodes[uf->size].index = index;
    uf->nodes[uf->size].parent = index;
    uf->nodes[uf->size].rank = 0;
    return uf->size++;
}

static bool hasNode(UnionFind* uf, int index) {
    return findNode(uf, index) != -1;
}

static bool unite(UnionFind* uf, int left, int right) {
    int rootLeft = findNode(uf, left);
    int rootRight = findNode(uf, right);
    if (rootLeft == -1 || rootRight == -1 || rootLeft == rootRight) {
        return false;
    }

    int leftPosition = -1;
    int rightPosition = -1;
    for (int position = 0; position < uf->size; position++) {
        if (uf->nodes[position].index == rootLeft) {
            leftPosition = position;
        }
        if (uf->nodes[position].index == rootRight) {
            rightPosition = position;
        }
    }

    if (uf->nodes[leftPosition].rank < uf->nodes[rightPosition].rank) {
        int temp = leftPosition;
        leftPosition = rightPosition;
        rightPosition = temp;
    }
    uf->nodes[rightPosition].parent = uf->nodes[leftPosition].index;
    if (uf->nodes[leftPosition].rank == uf->nodes[rightPosition].rank) {
        uf->nodes[leftPosition].rank += 1;
    }
    return true;
}

int* numIslands2(int m, int n, int** positions, int positionsSize, int* positionsColSize, int* returnSize) {
    (void)positionsColSize;
    UnionFind uf = { NULL, 0, 0 };
    int* result = (int*)malloc((size_t)positionsSize * sizeof(int));
    *returnSize = positionsSize;
    int islands = 0;
    const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    for (int positionIndex = 0; positionIndex < positionsSize; positionIndex++) {
        int row = positions[positionIndex][0];
        int col = positions[positionIndex][1];
        int index = row * n + col;
        if (hasNode(&uf, index)) {
            result[positionIndex] = islands;
            continue;
        }
        addNode(&uf, index);
        islands += 1;
        for (int directionIndex = 0; directionIndex < 4; directionIndex++) {
            int nextRow = row + directions[directionIndex][0];
            int nextCol = col + directions[directionIndex][1];
            if (nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n) {
                int neighbor = nextRow * n + nextCol;
                if (hasNode(&uf, neighbor) && unite(&uf, index, neighbor)) {
                    islands -= 1;
                }
            }
        }
        result[positionIndex] = islands;
    }

    free(uf.nodes);
    return result;
}
