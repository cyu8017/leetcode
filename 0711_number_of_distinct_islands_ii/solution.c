// LeetCode 0711 - Number of Distinct Islands II
// https://leetcode.com/problems/number-of-distinct-islands-ii/

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct {
    int x, y;
} Point;

static int cmpPoint(const void* a, const void* b) {
    const Point* p = a;
    const Point* q = b;
    if (p->x != q->x) {
        return p->x - q->x;
    }
    return p->y - q->y;
}

static void dfs(int** grid, int m, int n, int r, int c, Point* cells, int* count) {
    if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0) {
        return;
    }
    grid[r][c] = 0;
    cells[(*count)++] = (Point){r, c};
    dfs(grid, m, n, r + 1, c, cells, count);
    dfs(grid, m, n, r - 1, c, cells, count);
    dfs(grid, m, n, r, c + 1, cells, count);
    dfs(grid, m, n, r, c - 1, cells, count);
}

static void transform(Point* src, int len, Point* dst, int t) {
    for (int i = 0; i < len; i++) {
        int x = src[i].x, y = src[i].y;
        switch (t) {
            case 0: dst[i] = (Point){x, y}; break;
            case 1: dst[i] = (Point){x, -y}; break;
            case 2: dst[i] = (Point){-x, y}; break;
            case 3: dst[i] = (Point){-x, -y}; break;
            case 4: dst[i] = (Point){y, x}; break;
            case 5: dst[i] = (Point){y, -x}; break;
            case 6: dst[i] = (Point){-y, x}; break;
            default: dst[i] = (Point){-y, -x}; break;
        }
    }
}

static void normalize(Point* pts, int len, char* buf, size_t bufSize) {
    int minX = pts[0].x, minY = pts[0].y;
    for (int i = 1; i < len; i++) {
        if (pts[i].x < minX) minX = pts[i].x;
        if (pts[i].y < minY) minY = pts[i].y;
    }
    for (int i = 0; i < len; i++) {
        pts[i].x -= minX;
        pts[i].y -= minY;
    }
    qsort(pts, (size_t)len, sizeof(Point), cmpPoint);
    size_t pos = 0;
    for (int i = 0; i < len; i++) {
        pos += (size_t)snprintf(buf + pos, bufSize - pos, "%d,%d;", pts[i].x, pts[i].y);
    }
}

static void canonical(Point* cells, int len, char* best, size_t bestSize) {
    Point* tmp = (Point*)malloc((size_t)len * sizeof(Point));
    char* buf = (char*)malloc(bestSize);
    best[0] = '\0';
    for (int t = 0; t < 8; t++) {
        transform(cells, len, tmp, t);
        normalize(tmp, len, buf, bestSize);
        if (best[0] == '\0' || strcmp(buf, best) < 0) {
            strncpy(best, buf, bestSize - 1);
            best[bestSize - 1] = '\0';
        }
    }
    free(tmp);
    free(buf);
}

int numDistinctIslands2(int** grid, int gridSize, int* gridColSize) {
    if (gridSize == 0) {
        return 0;
    }
    int m = gridSize, n = gridColSize[0];
    char** shapes = (char**)malloc((size_t)(m * n + 1) * sizeof(char*));
    int shapeCount = 0;
    Point* cells = (Point*)malloc((size_t)(m * n) * sizeof(Point));
    size_t shapeCap = (size_t)(m * n * 16 + 64);
    char* shape = (char*)malloc(shapeCap);

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 1) {
                int count = 0;
                dfs(grid, m, n, i, j, cells, &count);
                canonical(cells, count, shape, shapeCap);
                int found = 0;
                for (int k = 0; k < shapeCount; k++) {
                    if (strcmp(shapes[k], shape) == 0) {
                        found = 1;
                        break;
                    }
                }
                if (!found) {
                    shapes[shapeCount] = (char*)malloc(strlen(shape) + 1);
                    strcpy(shapes[shapeCount], shape);
                    shapeCount++;
                }
            }
        }
    }

    for (int i = 0; i < shapeCount; i++) {
        free(shapes[i]);
    }
    free(shapes);
    free(cells);
    free(shape);
    return shapeCount;
}
