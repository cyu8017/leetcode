#include <string>
#include <vector>

class Solution {
public:
    bool canConstruct(std::string s, int k) {
        if (k > (int)s.size()) return false;
        std::vector<int> cnt(26, 0);
        for (char c : s) ++cnt[c - 'a'];
        int odd = 0;
        for (int v : cnt) odd += v % 2;
        return odd <= k;
    }
};
