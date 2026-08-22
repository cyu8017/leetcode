// LeetCode 3394 - Check if Grid can be Cut into Sections
// https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int a, b; } Seg;
static int cmp_seg(const void* x, const void* y) {
    const Seg* p = x; const Seg* q = y;
    if (p->a != q->a) return p->a - q->a;
    return p->b - q->b;
}
static bool checkCut(int** rects, int n, int axis) {
    Seg* arr = (Seg*)malloc(n * sizeof(Seg));
    for (int i = 0; i < n; i++) {
        if (axis == 0) arr[i] = (Seg){rects[i][0], rects[i][2]};
        else arr[i] = (Seg){rects[i][1], rects[i][3]};
    }
    qsort(arr, n, sizeof(Seg), cmp_seg);
    int cuts = 0, end = arr[0].b;
    for (int i = 1; i < n; i++) {
        if (arr[i].a >= end) {
            cuts++; end = arr[i].b;
            if (cuts >= 2) { free(arr); return true; }
        } else if (arr[i].b > end) end = arr[i].b;
    }
    free(arr);
    return false;
}

bool checkValidCuts(int n, int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    (void)n; (void)rectanglesColSize;
    return checkCut(rectangles, rectanglesSize, 0) || checkCut(rectangles, rectanglesSize, 1);
}
