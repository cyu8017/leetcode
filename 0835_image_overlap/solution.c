// LeetCode 0835 - Image Overlap
// https://leetcode.com/problems/image-overlap/

#include <stdlib.h>

#define MAX(a,b) ((a)>(b)?(a):(b))

int largestOverlap(int** img1, int img1Size, int* img1ColSize, int** img2, int img2Size, int* img2ColSize) {
    (void)img1ColSize; (void)img2Size; (void)img2ColSize;
    int n = img1Size;
    int ones1[900][2], ones2[900][2], n1 = 0, n2 = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (img1[i][j]) { ones1[n1][0]=i; ones1[n1][1]=j; n1++; }
            if (img2[i][j]) { ones2[n2][0]=i; ones2[n2][1]=j; n2++; }
        }
    if (!n1 || !n2) return 0;
    // map shift -> count; shift key = (dx+n)* (2n+1) + (dy+n)
    int dim = 2 * n + 1;
    int* cnt = (int*)calloc((size_t)dim * (size_t)dim, sizeof(int));
    int best = 0;
    for (int a = 0; a < n1; a++)
        for (int b = 0; b < n2; b++) {
            int dx = ones1[a][0] - ones2[b][0] + n;
            int dy = ones1[a][1] - ones2[b][1] + n;
            int k = dx * dim + dy;
            cnt[k]++;
            best = MAX(best, cnt[k]);
        }
    free(cnt);
    return best;
}
