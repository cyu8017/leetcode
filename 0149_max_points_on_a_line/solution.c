// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

#include <stdlib.h>

typedef struct {
    int dx;
    int dy;
    int count;
    int used;
} Slope;

static int gcd(int a, int b) {
    if (a < 0) a = -a;
    if (b < 0) b = -b;
    while (b) {
        int temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

int maxPoints(int **points, int pointsSize, int *pointsColSize) {
    (void)pointsColSize;
    if (pointsSize <= 2) return pointsSize;
    int best = 1;
    int table_size = pointsSize * 4 + 1;

    for (int i = 0; i < pointsSize; ++i) {
        Slope *table = calloc(table_size, sizeof(*table));
        int local = 1;
        for (int j = i + 1; j < pointsSize; ++j) {
            int dx = points[j][0] - points[i][0];
            int dy = points[j][1] - points[i][1];
            int divisor = gcd(dx, dy);
            dx /= divisor;
            dy /= divisor;
            if (dx < 0 || (dx == 0 && dy < 0)) {
                dx = -dx;
                dy = -dy;
            }
            unsigned index = ((unsigned)dx * 1000003u ^ (unsigned)dy) % table_size;
            while (table[index].used &&
                   (table[index].dx != dx || table[index].dy != dy)) {
                index = (index + 1) % table_size;
            }
            if (!table[index].used) {
                table[index] = (Slope){dx, dy, 0, 1};
            }
            ++table[index].count;
            if (table[index].count + 1 > local) local = table[index].count + 1;
        }
        if (local > best) best = local;
        free(table);
    }
    return best;
}
