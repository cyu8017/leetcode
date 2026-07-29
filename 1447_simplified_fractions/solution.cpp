#include <numeric>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> simplifiedFractions(int n) {
        std::vector<std::string> answer;
        for (int a = 1; a < n; ++a)
            for (int b = a + 1; b <= n; ++b)
                if (std::gcd(a, b) == 1) answer.push_back(std::to_string(a) + "/" + std::to_string(b));
        return answer;
    }
};
