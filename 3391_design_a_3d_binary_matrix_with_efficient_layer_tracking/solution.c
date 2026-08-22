// LeetCode 3391 - Design a 3D Binary Matrix with Efficient Layer Tracking
// https://leetcode.com/problems/design-a-3d-binary-matrix-with-efficient-layer-tracking/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int*** m;
    int* ones;
    int n;
} Matrix3D;

Matrix3D* matrix3DCreate(int n) {
    Matrix3D* obj = (Matrix3D*)malloc(sizeof(Matrix3D));
    obj->n = n;
    obj->ones = (int*)calloc(n, sizeof(int));
    obj->m = (int***)malloc(n * sizeof(int**));
    for (int i = 0; i < n; i++) {
        obj->m[i] = (int**)malloc(n * sizeof(int*));
        for (int j = 0; j < n; j++) obj->m[i][j] = (int*)calloc(n, sizeof(int));
    }
    return obj;
}

void matrix3DSetCell(Matrix3D* obj, int x, int y, int z) {
    if (obj->m[x][y][z] == 0) { obj->m[x][y][z] = 1; obj->ones[x]++; }
}

void matrix3DUnsetCell(Matrix3D* obj, int x, int y, int z) {
    if (obj->m[x][y][z] == 1) { obj->m[x][y][z] = 0; obj->ones[x]--; }
}

int matrix3DLargestMatrix(Matrix3D* obj) {
    int best = -1, idx = 0;
    for (int i = 0; i < obj->n; i++) if (obj->ones[i] >= best) { best = obj->ones[i]; idx = i; }
    return idx;
}

void matrix3DFree(Matrix3D* obj) {
    for (int i = 0; i < obj->n; i++) {
        for (int j = 0; j < obj->n; j++) free(obj->m[i][j]);
        free(obj->m[i]);
    }
    free(obj->m); free(obj->ones); free(obj);
}
