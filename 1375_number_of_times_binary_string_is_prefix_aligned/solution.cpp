#include <algorithm>
#include <vector>

class Solution {
public:
    int numTimesAllBlue(std::vector<int>& flips) {
        int ans = 0, mx = 0;
        for (int i = 0; i < (int)flips.size(); ++i) {
            mx = std::max(mx, flips[i]);
            ans += mx == i + 1;
        }
        return ans;
    }
};
