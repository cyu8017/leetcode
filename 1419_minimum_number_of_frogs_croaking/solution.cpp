#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int minNumberOfFrogs(std::string croakOfFrogs) {
        std::unordered_map<char, int> order{{'c',0},{'r',1},{'o',2},{'a',3},{'k',4}};
        std::vector<int> counts(5, 0);
        int active = 0, answer = 0;
        for (char ch : croakOfFrogs) {
            if (!order.count(ch)) return -1;
            int i = order[ch];
            if (i && counts[i - 1] == 0) return -1;
            if (i) --counts[i - 1];
            ++counts[i];
            if (i == 0) {
                ++active;
                answer = std::max(answer, active);
            } else if (i == 4) {
                --counts[4];
                --active;
            }
        }
        return active == 0 ? answer : -1;
    }
};
