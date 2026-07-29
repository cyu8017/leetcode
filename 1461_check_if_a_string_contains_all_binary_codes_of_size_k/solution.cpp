#include <string>
#include <unordered_set>

class Solution {
public:
    bool hasAllCodes(std::string s, int k) {
        if ((int)s.size() < k) return false;
        std::unordered_set<std::string> seen;
        for (int i = 0; i + k <= (int)s.size(); ++i)
            seen.insert(s.substr(i, k));
        return (int)seen.size() == (1 << k);
    }
};
