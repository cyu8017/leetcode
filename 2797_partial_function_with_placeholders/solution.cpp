// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/
// JS-only problem; C++ stand-in with nullable placeholders as INT_MIN sentinel.

#include <climits>
#include <functional>
#include <vector>

class Solution {
public:
    std::function<int(std::vector<int>)> partial(std::function<int(std::vector<int>)> fn, std::vector<int> args) {
        return [fn, args](std::vector<int> rest) {
            std::vector<int> full;
            int ri = 0;
            for (int a : args) {
                if (a == INT_MIN) {
                    if (ri < (int)rest.size()) full.push_back(rest[ri++]);
                } else {
                    full.push_back(a);
                }
            }
            while (ri < (int)rest.size()) full.push_back(rest[ri++]);
            return fn(full);
        };
    }
};
