#include <string>
#include <vector>

class Solution {
    bool valid(int value) {
        return std::to_string(value).find('0') == std::string::npos;
    }
public:
    std::vector<int> getNoZeroIntegers(int n) {
        for (int first = 1; first < n; ++first)
            if (valid(first) && valid(n - first)) return {first, n - first};
        return {};
    }
};
