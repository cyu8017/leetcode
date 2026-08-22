// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

#include <stdbool.h>
#include <stdlib.h>

typedef struct {
    int** vec;
    int* colSizes;
    int vecSize;
    int row;
    int col;
} Vector2D;

static void advance(Vector2D* obj) {
    while (obj->row < obj->vecSize && obj->col >= obj->colSizes[obj->row]) {
        obj->row += 1;
        obj->col = 0;
    }
}

Vector2D* vector2DCreate(int** vec, int vecSize, int* vecColSize) {
    Vector2D* obj = malloc(sizeof(*obj));
    obj->vec = vec;
    obj->colSizes = vecColSize;
    obj->vecSize = vecSize;
    obj->row = 0;
    obj->col = 0;
    advance(obj);
    return obj;
}

int vector2DNext(Vector2D* obj) {
    int value = obj->vec[obj->row][obj->col];
    obj->col += 1;
    advance(obj);
    return value;
}

bool vector2DHasNext(Vector2D* obj) {
    advance(obj);
    return obj->row < obj->vecSize;
}

void vector2DFree(Vector2D* obj) {
    free(obj);
}
