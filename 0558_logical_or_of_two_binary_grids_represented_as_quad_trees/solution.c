// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

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

struct Node* intersect(struct Node* quadTree1, struct Node* quadTree2) {
    if (quadTree1->isLeaf) {
        return quadTree1->val ? quadTree1 : quadTree2;
    }
    if (quadTree2->isLeaf) {
        return quadTree2->val ? quadTree2 : quadTree1;
    }

    struct Node* topLeft = intersect(quadTree1->topLeft, quadTree2->topLeft);
    struct Node* topRight = intersect(quadTree1->topRight, quadTree2->topRight);
    struct Node* bottomLeft = intersect(quadTree1->bottomLeft, quadTree2->bottomLeft);
    struct Node* bottomRight = intersect(quadTree1->bottomRight, quadTree2->bottomRight);

    if (topLeft->isLeaf && topRight->isLeaf && bottomLeft->isLeaf && bottomRight->isLeaf
        && topLeft->val == topRight->val && topRight->val == bottomLeft->val && bottomLeft->val == bottomRight->val) {
        return newNode(topLeft->val, true, NULL, NULL, NULL, NULL);
    }
    return newNode(false, false, topLeft, topRight, bottomLeft, bottomRight);
}
