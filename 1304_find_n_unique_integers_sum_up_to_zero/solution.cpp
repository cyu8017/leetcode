#include <vector>

class Solution {
public:
    std::vector<int> sumZero(int n) {
        std::vector<int> answer;
        for (int value = 1; value <= n / 2; ++value) {
            answer.push_back(-value);
            answer.push_back(value);
        }
        if (n % 2) answer.push_back(0);
        return answer;
    }
};
