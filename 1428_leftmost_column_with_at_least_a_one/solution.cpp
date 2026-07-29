#include <vector>

class BinaryMatrix {
public:
    int get(int row, int col);
    std::vector<int> dimensions();
};

class Solution {
public:
    int leftMostColumnWithOne(BinaryMatrix &binaryMatrix) {
        auto dim = binaryMatrix.dimensions();
        int rows = dim[0], cols = dim[1];
        int row = 0, col = cols - 1, answer = -1;
        while (row < rows && col >= 0) {
            if (binaryMatrix.get(row, col) == 1) {
                answer = col;
                --col;
            } else ++row;
        }
        return answer;
    }
};
