#include <string>

class Solution {
public:
    int numSteps(std::string s) {
        int steps = 0, carry = 0;
        for (int i = (int)s.size() - 1; i >= 1; --i) {
            int value = (s[i] - '0') + carry;
            if (value == 1) { steps += 2; carry = 1; }
            else ++steps;
        }
        return steps + carry;
    }
};
