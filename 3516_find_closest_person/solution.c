// LeetCode 3516 - Find Closest Person
// https://leetcode.com/problems/find-closest-person/

int findClosest(int x, int y, int z) {
    int dx = x - z; if (dx < 0) dx = -dx;
    int dy = y - z; if (dy < 0) dy = -dy;
    if (dx < dy) return 1;
    if (dy < dx) return 2;
    return 0;
}
