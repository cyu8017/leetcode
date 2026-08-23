// LeetCode 3915 - Maximum Sum Of Alternating Subsequence With Distance At Least K
// https://leetcode.com/problems/maximum-sum-of-alternating-subsequence-with-distance-at-least-k/

#include <algorithm>
#include <vector>

class Solution {
    struct Fenwick {
        std::vector<long long> f;
        explicit Fenwick(int n) : f(n, 0) {}
        void update(int i, long long val) {
            for (; i < (int)f.size(); i += i & -i) f[i] = std::max(f[i], val);
        }
        long long preMax(int i) {
            long long res = 0;
            for (; i > 0; i &= i - 1) res = std::max(res, f[i]);
            return res;
        }
    };

public:
    long long maxAlternatingSum(std::vector<int>& nums, int k) {
        std::vector<int> sorted = nums;
        std::sort(sorted.begin(), sorted.end());
        sorted.erase(std::unique(sorted.begin(), sorted.end()), sorted.end());
        int n = (int)nums.size();
        int m = (int)sorted.size();
        std::vector<long long> fInc(n), fDec(n);
        Fenwick inc(m + 1), dec(m + 1);
        long long ans = 0;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (i >= k) {
                int j = nums[i - k];
                inc.update(m - j, fInc[i - k]);
                dec.update(j + 1, fDec[i - k]);
            }
            int j = (int)(std::lower_bound(sorted.begin(), sorted.end(), x) - sorted.begin());
            nums[i] = j;
            fInc[i] = dec.preMax(j) + x;
            fDec[i] = inc.preMax(m - 1 - j) + x;
            ans = std::max({ans, fInc[i], fDec[i]});
        }
        return ans;
    }
};
