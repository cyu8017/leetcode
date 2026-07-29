#include <string>
#include <vector>

class Solution {
public:
    std::vector<std::string> buildArray(std::vector<int>& target, int n) {
        std::vector<std::string> answer;
        int current = 1;
        for (int value : target) {
            while (current < value) {
                answer.push_back("Push");
                answer.push_back("Pop");
                ++current;
            }
            answer.push_back("Push");
            ++current;
        }
        return answer;
    }
};
