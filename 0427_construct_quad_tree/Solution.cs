// LeetCode 0427 - Construct Quad Tree
// https://leetcode.com/problems/construct-quad-tree/

public class Node {
    public bool val;
    public bool isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
    public Node() { }
    public Node(bool val, bool isLeaf) {
        this.val = val;
        this.isLeaf = isLeaf;
    }
    public Node(bool val, bool isLeaf, Node topLeft, Node topRight, Node bottomLeft, Node bottomRight) {
        this.val = val;
        this.isLeaf = isLeaf;
        this.topLeft = topLeft;
        this.topRight = topRight;
        this.bottomLeft = bottomLeft;
        this.bottomRight = bottomRight;
    }
}

public class Solution {
    public Node Construct(int[][] grid) {
        Node Build(int row, int col, int size) {
            if (size == 1) {
                return new Node(grid[row][col] == 1, true);
            }

            int half = size / 2;
            Node topLeft = Build(row, col, half);
            Node topRight = Build(row, col + half, half);
            Node bottomLeft = Build(row + half, col, half);
            Node bottomRight = Build(row + half, col + half, half);

            if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf
                    && topLeft.val == topRight.val && topLeft.val == bottomLeft.val
                    && topLeft.val == bottomRight.val) {
                return new Node(topLeft.val, true);
            }

            return new Node(true, false, topLeft, topRight, bottomLeft, bottomRight);
        }

        return Build(0, 0, grid.Length);
    }
}
