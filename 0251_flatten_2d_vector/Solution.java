// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

class Vector2D {
    private final int[][] vec;
    private int row;
    private int col;

    public Vector2D(int[][] vec) {
        this.vec = vec;
        this.row = 0;
        this.col = 0;
        advance();
    }

    public int next() {
        int value = vec[row][col];
        col += 1;
        advance();
        return value;
    }

    public boolean hasNext() {
        advance();
        return row < vec.length;
    }

    private void advance() {
        while (row < vec.length && col >= vec[row].length) {
            row += 1;
            col = 0;
        }
    }
}
