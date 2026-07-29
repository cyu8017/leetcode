#include <algorithm>
#include <vector>

class Solution {
public:
    int maxSatisfaction(std::vector<int>& satisfaction) {
        std::sort(satisfaction.rbegin(), satisfaction.rend());
        int total = 0, answer = 0;
        for (int value : satisfaction) {
            if (total + value <= 0) break;
            total += value;
            answer += total;
        }
        return answer;
    }
};
