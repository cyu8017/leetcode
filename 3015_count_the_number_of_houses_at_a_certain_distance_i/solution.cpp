// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

#include <algorithm>
#include <cstdlib>
#include <vector>

class Solution {
public:
    std::vector<int> countOfPairs(int n, int x, int y) {
        std::vector<int> ans(n);
        x--; y--;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int a = j - i;
                int b = std::abs(x - i) + std::abs(y - j) + 1;
                int c = std::abs(x - j) + std::abs(y - i) + 1;
                ans[std::min({a, b, c}) - 1] += 2;
            }
        }
        return ans;
    }
};
