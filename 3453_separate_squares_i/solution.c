// LeetCode 3453 - Separate Squares I
// https://leetcode.com/problems/separate-squares-i/

double separateSquares(int** squares, int squaresSize, int* squaresColSize) {
    (void)squaresColSize;
    double total = 0.0;
    for (int i = 0; i < squaresSize; i++) {
        double l = (double)squares[i][2];
        total += l * l;
    }
    double lo = 0.0, hi = 2e9;
    for (int it = 0; it < 60; it++) {
        double mid = (lo + hi) / 2.0;
        double below = 0.0;
        for (int i = 0; i < squaresSize; i++) {
            double yi = (double)squares[i][1];
            double l = (double)squares[i][2];
            double top = yi + l;
            if (mid <= yi) continue;
            if (mid >= top) below += l * l;
            else below += l * (mid - yi);
        }
        if (below * 2.0 < total) lo = mid;
        else hi = mid;
    }
    return hi;
}
