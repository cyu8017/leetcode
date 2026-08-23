// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

#include <vector>

class Solution {
public:
    int numberOfWays(int n, int m, int k, std::vector<int>& source, std::vector<int>& dest) {
        const int mod = 1000000007;
        int sx = source[0], sy = source[1], tx = dest[0], ty = dest[1];
        long long same = 0, row = 0, col = 0, other = 0;
        if (sx == tx && sy == ty) same = 1;
        else if (sx == tx) row = 1;
        else if (sy == ty) col = 1;
        else other = 1;
        for (int step = 0; step < k; step++) {
            long long ns = (row * (m - 1) + col * (n - 1)) % mod;
            long long nr = (same + row * (m - 2) % mod + other * (n - 1) % mod) % mod;
            long long nc = (same + col * (n - 2) % mod + other * (m - 1) % mod) % mod;
            long long no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4) % mod) % mod;
            same = ns; row = nr; col = nc; other = no;
        }
        if (sx == tx && sy == ty) return (int)same;
        if (sx == tx) return (int)row;
        if (sy == ty) return (int)col;
        return (int)other;
    }
};
