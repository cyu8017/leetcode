// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

#include <functional>
#include <optional>
#include <string>

class Solution {
public:
    bool splitString(std::string s) {
        int n = static_cast<int>(s.size());

        std::function<bool(int, std::optional<long long>, int)> dfs =
            [&](int index, std::optional<long long> previous, int parts) -> bool {
            if (index == n) {
                return parts >= 2;
            }
            long long value = 0;
            for (int end = index; end < n; ++end) {
                value = value * 10 + (s[end] - '0');
                if (!previous.has_value()) {
                    if (dfs(end + 1, value, parts + 1)) {
                        return true;
                    }
                } else if (value == previous.value() - 1) {
                    if (dfs(end + 1, value, parts + 1)) {
                        return true;
                    }
                } else if (value > previous.value() - 1) {
                    break;
                }
            }
            return false;
        };

        return dfs(0, std::nullopt, 0);
    }
};
