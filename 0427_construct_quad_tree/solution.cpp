// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

#include <vector>

class Node {
public:
    bool val;
    bool isLeaf;
    Node* topLeft;
    Node* topRight;
    Node* bottomLeft;
    Node* bottomRight;

    Node()
        : val(false),
          isLeaf(false),
          topLeft(nullptr),
          topRight(nullptr),
          bottomLeft(nullptr),
          bottomRight(nullptr) {}

    Node(bool _val, bool _isLeaf)
        : val(_val),
          isLeaf(_isLeaf),
          topLeft(nullptr),
          topRight(nullptr),
          bottomLeft(nullptr),
          bottomRight(nullptr) {}

    Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight)
        : val(_val),
          isLeaf(_isLeaf),
          topLeft(_topLeft),
          topRight(_topRight),
          bottomLeft(_bottomLeft),
          bottomRight(_bottomRight) {}
};

class Solution {
    Node* build(const std::vector<std::vector<int>>& grid, int row, int col, int size) {
        if (size == 1) {
            return new Node(grid[row][col] == 1, true);
        }

        int half = size / 2;
        Node* topLeft = build(grid, row, col, half);
        Node* topRight = build(grid, row, col + half, half);
        Node* bottomLeft = build(grid, row + half, col, half);
        Node* bottomRight = build(grid, row + half, col + half, half);

        if (topLeft->isLeaf && topRight->isLeaf && bottomLeft->isLeaf && bottomRight->isLeaf &&
            topLeft->val == topRight->val && topLeft->val == bottomLeft->val &&
            topLeft->val == bottomRight->val) {
            bool value = topLeft->val;
            delete topLeft;
            delete topRight;
            delete bottomLeft;
            delete bottomRight;
            return new Node(value, true);
        }

        return new Node(true, false, topLeft, topRight, bottomLeft, bottomRight);
    }

public:
    Node* construct(std::vector<std::vector<int>>& grid) {
        return build(grid, 0, 0, static_cast<int>(grid.size()));
    }
};
