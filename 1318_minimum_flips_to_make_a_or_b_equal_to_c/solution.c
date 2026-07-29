// LeetCode 1318 - Minimum Flips to Make a OR b Equal to c
// https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

int minFlips(int a, int b, int c) {
    int flips = 0;
    while (a || b || c) {
        int x = a & 1, y = b & 1, z = c & 1;
        if (z == 0) flips += x + y;
        else flips += (x == 0 && y == 0);
        a >>= 1; b >>= 1; c >>= 1;
    }
    return flips;
}
