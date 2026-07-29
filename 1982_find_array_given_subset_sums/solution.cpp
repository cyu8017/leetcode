// LeetCode 1982 - Find Array Given Subset Sums
#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> recoverArray(int n, std::vector<int>& sums) {
        std::sort(sums.begin(), sums.end());
        std::vector<int> ans;
        for (int t = 0; t < n; t++) {
            int d = sums[1] - sums[0];
            std::unordered_map<int, int> count;
            for (int x : sums) count[x]++;
            std::vector<int> without, withD;
            for (int x : sums) {
                if (count[x] == 0) continue;
                count[x]--;
                count[x + d]--;
                without.push_back(x);
                withD.push_back(x + d);
            }
            bool hasZero = false;
            for (int x : without) if (x == 0) { hasZero = true; break; }
            if (hasZero) {
                ans.push_back(d);
                sums = without;
            } else {
                ans.push_back(-d);
                sums = withD;
            }
        }
        return ans;
    }
};
