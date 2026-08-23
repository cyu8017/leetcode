// LeetCode 2320 - Count Number of Ways to Place Houses
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution {
public:
    int countHousePlacements(int n) {
        const int mod = 1000000007;
        long long a = 1, b = 1;
        for (int i = 1; i <= n; ++i) {
            long long na = (a + b) % mod;
            b = a;
            a = na;
        }
        long long ways = (a + b) % mod;
        return (int)(ways * ways % mod);
    }
};
