// LeetCode 3783 - Mirror Distance Of An Integer
// https://leetcode.com/problems/mirror-distance-of-an-integer/

int mirrorDistance(int n) {
    int x = n, y = 0;
    for (; x > 0; x /= 10) y = y * 10 + x % 10;
    int d = n - y;
    return d < 0 ? -d : d;
}
