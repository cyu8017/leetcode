// LeetCode 1349 - Maximum Students Taking Exam
// https://leetcode.com/problems/maximum-students-taking-exam/

#include <stdlib.h>
#include <string.h>

static int bitcount(int x) {
    int c = 0;
    while (x) { c += x & 1; x >>= 1; }
    return c;
}

int maxStudents(char** seats, int seatsSize, int* seatsColSize) {
    int rows = seatsSize, cols = seatsColSize[0];
    int* maskCount = (int*)calloc(rows, sizeof(int));
    int** valid = (int**)malloc(rows * sizeof(int*));
    for (int r = 0; r < rows; r++) {
        int available = 0;
        for (int c = 0; c < cols; c++) if (seats[r][c] == '.') available |= 1 << c;
        valid[r] = (int*)malloc((1 << cols) * sizeof(int));
        maskCount[r] = 0;
        for (int mask = 0; mask < (1 << cols); mask++) {
            if ((mask & ~available) == 0 && (mask & (mask << 1)) == 0)
                valid[r][maskCount[r]++] = mask;
        }
    }
    int* dp_mask = (int*)malloc((1 << cols) * sizeof(int));
    int* dp_val = (int*)malloc((1 << cols) * sizeof(int));
    int dpn = 1;
    dp_mask[0] = 0; dp_val[0] = 0;
    for (int r = 0; r < rows; r++) {
        int* nxt_mask = (int*)malloc((1 << cols) * sizeof(int));
        int* nxt_val = (int*)malloc((1 << cols) * sizeof(int));
        int nn = 0;
        for (int mi = 0; mi < maskCount[r]; mi++) {
            int mask = valid[r][mi];
            int best = -1;
            for (int pi = 0; pi < dpn; pi++) {
                int previous = dp_mask[pi];
                if ((mask & (previous << 1)) == 0 && (mask & (previous >> 1)) == 0) {
                    int cand = dp_val[pi] + bitcount(mask);
                    if (cand > best) best = cand;
                }
            }
            if (best >= 0) {
                nxt_mask[nn] = mask;
                nxt_val[nn] = best;
                nn++;
            }
        }
        free(dp_mask); free(dp_val);
        dp_mask = nxt_mask; dp_val = nxt_val; dpn = nn;
    }
    int ans = 0;
    for (int i = 0; i < dpn; i++) if (dp_val[i] > ans) ans = dp_val[i];
    for (int r = 0; r < rows; r++) free(valid[r]);
    free(valid); free(maskCount); free(dp_mask); free(dp_val);
    return ans;
}
