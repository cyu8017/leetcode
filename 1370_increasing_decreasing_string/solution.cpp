#include <string>
#include <vector>

class Solution {
public:
    std::string sortString(std::string s) {
        std::vector<int> c(26, 0);
        for (char ch : s) ++c[ch - 'a'];
        std::string out;
        while ((int)out.size() < (int)s.size()) {
            for (int i = 0; i < 26; ++i)
                if (c[i]) { out.push_back(char('a' + i)); --c[i]; }
            for (int i = 25; i >= 0; --i)
                if (c[i]) { out.push_back(char('a' + i)); --c[i]; }
        }
        return out;
    }
};
