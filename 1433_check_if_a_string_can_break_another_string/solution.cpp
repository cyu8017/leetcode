#include <algorithm>
#include <string>

class Solution {
public:
    bool checkIfCanBreak(std::string s1, std::string s2) {
        std::sort(s1.begin(), s1.end());
        std::sort(s2.begin(), s2.end());
        bool ge = true, le = true;
        for (size_t i = 0; i < s1.size(); ++i) {
            if (s1[i] < s2[i]) ge = false;
            if (s1[i] > s2[i]) le = false;
        }
        return ge || le;
    }
};
