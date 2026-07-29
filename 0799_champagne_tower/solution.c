// LeetCode 0799 - Champagne Tower
// https://leetcode.com/problems/champagne-tower/

double champagneTower(int poured, int query_row, int query_glass) {
    double row[101] = {0};
    row[0] = (double)poured;
    for (int r = 0; r < query_row; r++) {
        double next[101] = {0};
        for (int j = 0; j <= r; j++) {
            double excess = row[j] - 1.0;
            if (excess > 0) {
                next[j] += excess / 2.0;
                next[j + 1] += excess / 2.0;
            }
        }
        for (int j = 0; j <= r + 1; j++) row[j] = next[j];
    }
    return row[query_glass] > 1.0 ? 1.0 : row[query_glass];
}
