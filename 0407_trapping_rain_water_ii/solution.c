// LeetCode 0407 - Trapping Rain Water II
// https://leetcode.com/problems/trapping-rain-water-ii/

#include <stdlib.h>

typedef struct {
    int height;
    int row;
    int col;
} HeapEntry;

static int compare_heap_entries(const void* left, const void* right) {
    return ((const HeapEntry*)left)->height - ((const HeapEntry*)right)->height;
}

static void heap_push(HeapEntry* heap, int* heapSize, int height, int row, int col) {
    heap[*heapSize].height = height;
    heap[*heapSize].row = row;
    heap[*heapSize].col = col;
    *heapSize += 1;
    qsort(heap, (size_t)*heapSize, sizeof(HeapEntry), compare_heap_entries);
}

static HeapEntry heap_pop(HeapEntry* heap, int* heapSize) {
    HeapEntry top = heap[0];
    heap[0] = heap[*heapSize - 1];
    *heapSize -= 1;
    qsort(heap, (size_t)*heapSize, sizeof(HeapEntry), compare_heap_entries);
    return top;
}

static int max_int(int left, int right) {
    return left > right ? left : right;
}

int trapRainWater(int** heightMap, int heightMapSize, int* heightMapColSize) {
    if (heightMapSize == 0 || heightMapColSize[0] == 0) {
        return 0;
    }

    int rows = heightMapSize;
    int cols = heightMapColSize[0];
    if (rows < 3 || cols < 3) {
        return 0;
    }

    int cellCount = rows * cols;
    int* visited = (int*)calloc((size_t)cellCount, sizeof(int));
    int heapCapacity = cellCount;
    HeapEntry* heap = (HeapEntry*)malloc((size_t)heapCapacity * sizeof(HeapEntry));
    int heapSize = 0;

    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (row == 0 || row == rows - 1 || col == 0 || col == cols - 1) {
                heap_push(heap, &heapSize, heightMap[row][col], row, col);
                visited[row * cols + col] = 1;
            }
        }
    }

    const int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int trapped = 0;

    while (heapSize > 0) {
        HeapEntry top = heap_pop(heap, &heapSize);

        for (int directionIndex = 0; directionIndex < 4; directionIndex++) {
            int nextRow = top.row + directions[directionIndex][0];
            int nextCol = top.col + directions[directionIndex][1];
            if (nextRow < 0 || nextRow >= rows || nextCol < 0 || nextCol >= cols) {
                continue;
            }

            int visitIndex = nextRow * cols + nextCol;
            if (visited[visitIndex]) {
                continue;
            }

            visited[visitIndex] = 1;
            int nextHeight = heightMap[nextRow][nextCol];
            trapped += max_int(0, top.height - nextHeight);
            heap_push(heap, &heapSize, max_int(top.height, nextHeight), nextRow, nextCol);
        }
    }

    free(visited);
    free(heap);
    return trapped;
}
