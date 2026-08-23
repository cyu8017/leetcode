// LeetCode 3907 - Count Smaller Elements With Opposite Parity
// https://leetcode.com/problems/count-smaller-elements-with-opposite-parity/

#include <algorithm>
#include <vector>

class Solution {
    struct BIT {
        int n;
        std::vector<int> c;
        explicit BIT(int n_) : n(n_), c(n_ + 1, 0) {}
        void update(int x, int delta) {
            for (; x <= n; x += x & -x) c[x] += delta;
        }
        int query(int x) {
            int s = 0;
            for (; x > 0; x -= x & -x) s += c[x];
            return s;
        }
    };

public:
    std::vector<int> countSmallerOppositeParity(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        sorted.erase(std::unique(sorted.begin(), sorted.end()), sorted.end());
        int m = (int)sorted.size();
        BIT bits[2] = {BIT(m), BIT(m)};
        std::vector<int> ans(n);
        for (int i = n - 1; i >= 0; i--) {
            int x = (int)(std::lower_bound(sorted.begin(), sorted.end(), nums[i]) - sorted.begin()) + 1;
            ans[i] = bits[(nums[i] & 1) ^ 1].query(x - 1);
            bits[nums[i] & 1].update(x, 1);
        }
        return ans;
    }
};
