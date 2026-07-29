class Solution {
public:
    int minFlips(int a, int b, int c) {
        int flips = 0;
        while (a || b || c) {
            int x = a & 1, y = b & 1, z = c & 1;
            flips += z == 0 ? x + y : int(x == 0 && y == 0);
            a >>= 1; b >>= 1; c >>= 1;
        }
        return flips;
    }
};
