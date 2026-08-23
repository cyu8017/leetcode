// LeetCode 2300 - Successful Pairs of Spells and Potions
// https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> successfulPairs(std::vector<int>& spells, std::vector<int>& potions, long long success) {
        std::sort(potions.begin(), potions.end());
        int m = (int)potions.size();
        std::vector<int> ans(spells.size());
        for (size_t i = 0; i < spells.size(); ++i) {
            int lo = 0, hi = m;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (1LL * spells[i] * potions[mid] >= success) hi = mid;
                else lo = mid + 1;
            }
            ans[i] = m - lo;
        }
        return ans;
    }
};
