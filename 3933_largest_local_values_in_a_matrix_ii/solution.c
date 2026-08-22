// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

#include <stdlib.h>
#include <string.h>

static int min3933(int a, int b) { return a < b ? a : b; }
static int max3933(int a, int b) { return a > b ? a : b; }

int countLocalMaximums(int** matrix, int matrixSize, int* matrixColSize) {
    int rows = matrixSize, cols = matrixColSize[0];
    int* posR[201];
    int* posC[201];
    int psz[201];
    int pcap[201];
    memset(psz, 0, sizeof(psz));
    memset(pcap, 0, sizeof(pcap));
    memset(posR, 0, sizeof(posR));
    memset(posC, 0, sizeof(posC));
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            int value = matrix[row][col];
            if (value > 0) {
                if (psz[value] == pcap[value]) {
                    pcap[value] = pcap[value] ? pcap[value] * 2 : 4;
                    posR[value] = realloc(posR[value], (size_t)pcap[value] * sizeof(int));
                    posC[value] = realloc(posC[value], (size_t)pcap[value] * sizeof(int));
                }
                posR[value][psz[value]] = row;
                posC[value][psz[value]] = col;
                psz[value]++;
            }
        }
    }
    int answer = 0;
    for (int value = 1; value <= 200; value++) {
        if (!psz[value]) continue;
        int** prefix = malloc((size_t)(rows + 1) * sizeof(int*));
        for (int i = 0; i <= rows; i++) prefix[i] = calloc((size_t)(cols + 1), sizeof(int));
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int add = matrix[row][col] > value ? 1 : 0;
                prefix[row + 1][col + 1] = prefix[row][col + 1] + prefix[row + 1][col] - prefix[row][col] + add;
            }
        }
        for (int pi = 0; pi < psz[value]; pi++) {
            int row = posR[value][pi], col = posC[value][pi];
            int top = max3933(0, row - value), bottom = min3933(rows - 1, row + value);
            int left = max3933(0, col - value), right = min3933(cols - 1, col + value);
            int greater = prefix[bottom + 1][right + 1] - prefix[top][right + 1] - prefix[bottom + 1][left] + prefix[top][left];
            int drs[2] = {-value, value};
            for (int di = 0; di < 2; di++) for (int dj = 0; dj < 2; dj++) {
                int r = row + drs[di], c = col + drs[dj];
                if (r >= 0 && r < rows && c >= 0 && c < cols && matrix[r][c] > value) greater--;
            }
            if (greater == 0) answer++;
        }
        for (int i = 0; i <= rows; i++) free(prefix[i]);
        free(prefix);
    }
    for (int v = 0; v <= 200; v++) { free(posR[v]); free(posC[v]); }
    return answer;
}
