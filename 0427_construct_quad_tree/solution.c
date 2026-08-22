// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

#include <stdbool.h>
#include <stdlib.h>

struct Node {
    bool val;
    bool isLeaf;
    struct Node* topLeft;
    struct Node* topRight;
    struct Node* bottomLeft;
    struct Node* bottomRight;
};

static struct Node* newNode(bool val, bool isLeaf, struct Node* topLeft, struct Node* topRight, struct Node* bottomLeft, struct Node* bottomRight) {
    struct Node* node = (struct Node*)malloc(sizeof(struct Node));
    node->val = val;
    node->isLeaf = isLeaf;
    node->topLeft = topLeft;
    node->topRight = topRight;
    node->bottomLeft = bottomLeft;
    node->bottomRight = bottomRight;
    return node;
}

static struct Node* build(int** grid, int row, int col, int size) {
    if (size == 1) {
        return newNode(grid[row][col] != 0, true, NULL, NULL, NULL, NULL);
    }
    int half = size / 2;
    struct Node* topLeft = build(grid, row, col, half);
    struct Node* topRight = build(grid, row, col + half, half);
    struct Node* bottomLeft = build(grid, row + half, col, half);
    struct Node* bottomRight = build(grid, row + half, col + half, half);

    if (topLeft->isLeaf && topRight->isLeaf && bottomLeft->isLeaf && bottomRight->isLeaf
        && topLeft->val == topRight->val && topRight->val == bottomLeft->val && bottomLeft->val == bottomRight->val) {
        bool value = topLeft->val;
        free(topLeft);
        free(topRight);
        free(bottomLeft);
        free(bottomRight);
        return newNode(value, true, NULL, NULL, NULL, NULL);
    }
    return newNode(true, false, topLeft, topRight, bottomLeft, bottomRight);
}

struct Node* construct(int** grid, int gridSize, int* gridColSize) {
    (void)gridColSize;
    return build(grid, 0, 0, gridSize);
}
