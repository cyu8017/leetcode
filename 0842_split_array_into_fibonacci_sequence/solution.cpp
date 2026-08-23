// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

#include <climits>
#include <functional>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> splitIntoFibonacci(std::string num) {
        int n = static_cast<int>(num.size());
        std::vector<int> path;
        std::function<bool(int)> dfs = [&](int start) -> bool {
            if (start == n) {
                return path.size() >= 3;
            }
            long long val = 0;
            for (int end = start; end < n; ++end) {
                if (num[start] == '0' && end > start) {
                    break;
                }
                val = val * 10 + (num[end] - '0');
                if (val > INT_MAX) {
                    break;
                }
                if (path.size() >= 2) {
                    long long total =
                        static_cast<long long>(path.back()) + path[path.size() - 2];
                    if (val < total) {
                        continue;
                    }
                    if (val > total) {
                        break;
                    }
                }
                path.push_back(static_cast<int>(val));
                if (dfs(end + 1)) {
                    return true;
                }
                path.pop_back();
            }
            return false;
        };
        dfs(0);
        return path;
    }
};
