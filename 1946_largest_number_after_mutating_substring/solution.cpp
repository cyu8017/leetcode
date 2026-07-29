// LeetCode 1946 - Largest Number After Mutating Substring
#include <string>
#include <vector>

class Solution {
public:
    std::string maximumNumber(std::string num, std::vector<int>& change) {
        bool started = false;
        for (int i = 0; i < (int)num.size(); i++) {
            int d = num[i] - '0';
            int mapped = change[d];
            if (mapped > d) {
                num[i] = char('0' + mapped);
                started = true;
            } else if (mapped < d && started) break;
        }
        return num;
    }
};
