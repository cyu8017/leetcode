// LeetCode 0386 - Lexicographical Numbers
// https://leetcode.com/problems/lexicographical-numbers/

#include <functional>
#include <vector>

class Solution {
public:
    std::vector<int> lexicalOrder(int n) {
        std::vector<int> result;

        std::function<void(int)> dfs = [&](int current) {
            if (current > n) {
                return;
            }
            result.push_back(current);
            dfs(current * 10);
            if (current % 10 < 9) {
                dfs(current + 1);
            }
        };

        dfs(1);
        return result;
    }
};
