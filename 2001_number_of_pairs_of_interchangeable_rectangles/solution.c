// LeetCode 2001 - Number of Pairs of Interchangeable Rectangles
// https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

#include <stdlib.h>

static int gcd2001(int a, int b) {
    while (b) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

typedef struct {
    int w, h;
    int cnt;
    int used;
} RatioEntry;

long long interchangeableRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize) {
    (void)rectanglesColSize;
    int cap = 1024;
    while (cap < rectanglesSize * 2) cap *= 2;
    RatioEntry* tab = (RatioEntry*)calloc((size_t)cap, sizeof(RatioEntry));
    long long ans = 0;
    for (int i = 0; i < rectanglesSize; i++) {
        int w = rectangles[i][0], h = rectangles[i][1];
        int g = gcd2001(w, h);
        w /= g; h /= g;
        unsigned hash = (unsigned)w * 2654435761u ^ (unsigned)h * 40503u;
        int idx = (int)(hash & (unsigned)(cap - 1));
        for (;;) {
            if (!tab[idx].used) {
                tab[idx].used = 1;
                tab[idx].w = w;
                tab[idx].h = h;
                tab[idx].cnt = 1;
                break;
            }
            if (tab[idx].w == w && tab[idx].h == h) {
                ans += tab[idx].cnt;
                tab[idx].cnt++;
                break;
            }
            idx = (idx + 1) & (cap - 1);
        }
    }
    free(tab);
    return ans;
}
