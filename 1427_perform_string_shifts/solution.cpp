#include <string>
#include <vector>

class Solution {
public:
    std::string stringShift(std::string s, std::vector<std::vector<int>>& shift) {
        int offset = 0, n = (int)s.size();
        for (auto& sh : shift) offset += sh[0] ? sh[1] : -sh[1];
        offset %= n;
        if (offset < 0) offset += n;
        if (!offset) return s;
        return s.substr(n - offset) + s.substr(0, n - offset);
    }
};
