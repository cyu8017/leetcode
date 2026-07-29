#include <cmath>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int sumFourDivisors(std::vector<int>& nums) {
        int ans = 0;
        for (int x : nums) {
            std::unordered_set<int> ds;
            for (int d = 1; d * d <= x; ++d) {
                if (x % d == 0) { ds.insert(d); ds.insert(x / d); }
                if (ds.size() > 4) break;
            }
            if (ds.size() == 4) {
                for (int v : ds) ans += v;
            }
        }
        return ans;
    }
};
