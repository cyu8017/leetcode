// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<long long> countOfPairs(int n, int x, int y) {
        if (x > y) std::swap(x, y);
        std::vector<long long> A(n, 0);
        for (int i = 1; i <= n; i++) {
            A[0] += 2;
            A[std::min((long long)(i - 1), (long long)std::abs(i - y) + x)] -= 1;
            A[std::min((long long)(n - i), (long long)std::abs(i - x) + 1 + (n - y))] -= 1;
            A[std::min((long long)std::abs(i - x), (long long)std::abs(y - i) + 1)] += 1;
            A[std::min((long long)std::abs(i - x) + 1, (long long)std::abs(y - i))] += 1;
            long long r = std::max((long long)(x - i), 0LL) + std::max((long long)(i - y), 0LL);
            A[r + (y - x) / 2] -= 1;
            A[r + (y - x + 1) / 2] -= 1;
        }
        for (int i = 1; i < n; i++) A[i] += A[i - 1];
        return A;
    }
};
