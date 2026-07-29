#include <vector>

class Solution {
public:
    int numTeams(std::vector<int>& rating) {
        int ans = 0, n = (int)rating.size();
        for (int j = 0; j < n; ++j) {
            int ll = 0, lg = 0, rl = 0, rg = 0;
            for (int i = 0; i < j; ++i) (rating[i] < rating[j] ? ll : lg)++;
            for (int i = j + 1; i < n; ++i) (rating[i] > rating[j] ? rg : rl)++;
            ans += ll * rg + lg * rl;
        }
        return ans;
    }
};
