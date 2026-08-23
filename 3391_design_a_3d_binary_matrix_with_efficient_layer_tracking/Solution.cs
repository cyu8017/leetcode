// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

public class Matrix3D {
    int[][][] m;
    int[] ones;
    int n;

    public Matrix3D(int n) {
        this.n = n;
        m = new int[n][][];
        ones = new int[n];
        for (int i = 0; i < n; i++) {
            m[i] = new int[n][];
            for (int j = 0; j < n; j++) m[i][j] = new int[n];
        }
    }

    public void SetCell(int x, int y, int z) {
        if (m[x][y][z] == 0) {
            m[x][y][z] = 1;
            ones[x]++;
        }
    }

    public void UnsetCell(int x, int y, int z) {
        if (m[x][y][z] == 1) {
            m[x][y][z] = 0;
            ones[x]--;
        }
    }

    public int LargestMatrix() {
        int best = -1, idx = 0;
        for (int i = 0; i < n; i++) {
            if (ones[i] >= best) {
                best = ones[i];
                idx = i;
            }
        }
        return idx;
    }
}
