// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

#include <vector>

class Matrix3D {
    std::vector<std::vector<std::vector<int>>> m;
    std::vector<int> ones;
    int n;

public:
    Matrix3D(int n_) : m(n_, std::vector<std::vector<int>>(n_, std::vector<int>(n_, 0))), ones(n_, 0), n(n_) {}

    void setCell(int x, int y, int z) {
        if (m[x][y][z] == 0) {
            m[x][y][z] = 1;
            ones[x]++;
        }
    }

    void unsetCell(int x, int y, int z) {
        if (m[x][y][z] == 1) {
            m[x][y][z] = 0;
            ones[x]--;
        }
    }

    int largestMatrix() {
        int best = -1, idx = 0;
        for (int i = 0; i < n; i++) {
            if (ones[i] >= best) {
                best = ones[i];
                idx = i;
            }
        }
        return idx;
    }
};
