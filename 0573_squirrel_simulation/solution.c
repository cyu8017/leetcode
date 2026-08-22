// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

static int manhattan(int* a, int* b) {
    int dx = a[0] - b[0];
    int dy = a[1] - b[1];
    if (dx < 0) {
        dx = -dx;
    }
    if (dy < 0) {
        dy = -dy;
    }
    return dx + dy;
}

int minDistance(int height, int width, int* tree, int treeSize, int* squirrel, int squirrelSize, int** nuts, int nutsSize, int* nutsColSize) {
    (void)height;
    (void)width;
    (void)treeSize;
    (void)squirrelSize;
    (void)nutsColSize;
    int total = 0;
    int bestSave = -2147483647;
    for (int i = 0; i < nutsSize; i++) {
        int treeDist = manhattan(tree, nuts[i]);
        int squirrelDist = manhattan(squirrel, nuts[i]);
        total += 2 * treeDist;
        int save = treeDist - squirrelDist;
        if (save > bestSave) {
            bestSave = save;
        }
    }
    return total - bestSave;
}
