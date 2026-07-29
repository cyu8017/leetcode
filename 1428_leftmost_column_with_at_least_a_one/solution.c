// LeetCode 1428 - Leftmost Column with at Least a One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

typedef struct BinaryMatrix BinaryMatrix;

struct BinaryMatrix {
    int (*get)(struct BinaryMatrix*, int, int);
    int* (*dimensions)(struct BinaryMatrix*);
};

int leftMostColumnWithOne(BinaryMatrix* matrix) {
    int* dim = matrix->dimensions(matrix);
    int rows = dim[0], cols = dim[1];
    int row = 0, col = cols - 1, answer = -1;
    while (row < rows && col >= 0) {
        if (matrix->get(matrix, row, col) == 1) {
            answer = col;
            col--;
        } else {
            row++;
        }
    }
    return answer;
}
