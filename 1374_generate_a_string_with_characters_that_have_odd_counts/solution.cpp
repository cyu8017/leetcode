#include <string>

class Solution {
public:
    std::string generateTheString(int n) {
        if (n % 2) return std::string(n, 'a');
        return std::string(n - 1, 'a') + 'b';
    }
};
