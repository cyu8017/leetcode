// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

#include <stdlib.h>
#include <string.h>

static int containVirusImpl(int** g, int m, int n) {
    int walls = 0;
    int* seen = (int*)malloc((size_t)m * n * sizeof(int));
    int* stackR = (int*)malloc((size_t)m * n * sizeof(int));
    int* stackC = (int*)malloc((size_t)m * n * sizeof(int));
    int* regionR = (int*)malloc((size_t)m * n * sizeof(int));
    int* regionC = (int*)malloc((size_t)m * n * sizeof(int));
    int* frontierR = (int*)malloc((size_t)m * n * sizeof(int));
    int* frontierC = (int*)malloc((size_t)m * n * sizeof(int));
    int* frontierMark = (int*)malloc((size_t)m * n * sizeof(int));
    int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};

    while (1) {
        memset(seen, 0, (size_t)m * n * sizeof(int));
        int bestFrontier = -1, bestIdx = -1, regionCount = 0;
        int* regionSizes = (int*)calloc(200, sizeof(int));
        int* perimeters = (int*)calloc(200, sizeof(int));
        int** allRegionsR = (int**)calloc(200, sizeof(int*));
        int** allRegionsC = (int**)calloc(200, sizeof(int*));
        int** allFrontR = (int**)calloc(200, sizeof(int*));
        int** allFrontC = (int**)calloc(200, sizeof(int*));
        int* frontSizes = (int*)calloc(200, sizeof(int));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (g[i][j] != 1 || seen[i * n + j]) continue;
                int top = 0, rsize = 0, fsize = 0, peri = 0;
                stackR[top] = i; stackC[top] = j; top++;
                seen[i * n + j] = 1;
                memset(frontierMark, 0, (size_t)m * n * sizeof(int));
                while (top) {
                    top--;
                    int r = stackR[top], c = stackC[top];
                    regionR[rsize] = r; regionC[rsize] = c; rsize++;
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dirs[d][0], nc = c + dirs[d][1];
                        if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                        if (g[nr][nc] == 1 && !seen[nr * n + nc]) {
                            seen[nr * n + nc] = 1;
                            stackR[top] = nr; stackC[top] = nc; top++;
                        } else if (g[nr][nc] == 0) {
                            peri++;
                            if (!frontierMark[nr * n + nc]) {
                                frontierMark[nr * n + nc] = 1;
                                frontierR[fsize] = nr; frontierC[fsize] = nc; fsize++;
                            }
                        }
                    }
                }
                allRegionsR[regionCount] = (int*)malloc((size_t)rsize * sizeof(int));
                allRegionsC[regionCount] = (int*)malloc((size_t)rsize * sizeof(int));
                memcpy(allRegionsR[regionCount], regionR, (size_t)rsize * sizeof(int));
                memcpy(allRegionsC[regionCount], regionC, (size_t)rsize * sizeof(int));
                regionSizes[regionCount] = rsize;
                allFrontR[regionCount] = (int*)malloc((size_t)fsize * sizeof(int));
                allFrontC[regionCount] = (int*)malloc((size_t)fsize * sizeof(int));
                memcpy(allFrontR[regionCount], frontierR, (size_t)fsize * sizeof(int));
                memcpy(allFrontC[regionCount], frontierC, (size_t)fsize * sizeof(int));
                frontSizes[regionCount] = fsize;
                perimeters[regionCount] = peri;
                if (fsize > bestFrontier) {
                    bestFrontier = fsize;
                    bestIdx = regionCount;
                }
                regionCount++;
            }
        }

        if (regionCount == 0 || bestFrontier <= 0) {
            for (int i = 0; i < regionCount; i++) {
                free(allRegionsR[i]); free(allRegionsC[i]);
                free(allFrontR[i]); free(allFrontC[i]);
            }
            free(regionSizes); free(perimeters);
            free(allRegionsR); free(allRegionsC); free(allFrontR); free(allFrontC); free(frontSizes);
            break;
        }

        walls += perimeters[bestIdx];
        for (int i = 0; i < regionSizes[bestIdx]; i++) {
            g[allRegionsR[bestIdx][i]][allRegionsC[bestIdx][i]] = -1;
        }
        for (int idx = 0; idx < regionCount; idx++) {
            if (idx == bestIdx) continue;
            for (int i = 0; i < frontSizes[idx]; i++) {
                g[allFrontR[idx][i]][allFrontC[idx][i]] = 1;
            }
        }
        for (int i = 0; i < regionCount; i++) {
            free(allRegionsR[i]); free(allRegionsC[i]);
            free(allFrontR[i]); free(allFrontC[i]);
        }
        free(regionSizes); free(perimeters);
        free(allRegionsR); free(allRegionsC); free(allFrontR); free(allFrontC); free(frontSizes);
    }

    free(seen); free(stackR); free(stackC); free(regionR); free(regionC);
    free(frontierR); free(frontierC); free(frontierMark);
    return walls;
}

int containVirus(int** isInfected, int isInfectedSize, int* isInfectedColSize) {
    return containVirusImpl(isInfected, isInfectedSize, isInfectedColSize[0]);
}
