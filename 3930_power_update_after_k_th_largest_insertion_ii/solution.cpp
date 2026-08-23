// LeetCode 3930 - Power Update After K-th Largest Insertion II
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-ii/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> powerUpdate(std::vector<int>& nums, int p, std::vector<std::vector<int>>& queries) {
        const long long mod = 1000000007;
        std::vector<int> vals = nums;
        for (auto& q : queries) vals.push_back(q[0]);
        std::sort(vals.begin(), vals.end());
        vals.erase(std::unique(vals.begin(), vals.end()), vals.end());
        std::vector<int> bit(vals.size() + 1, 0);
        auto add = [&](int i) {
            for (; i < (int)bit.size(); i += i & -i) bit[i]++;
        };
        auto kth = [&](int rank) {
            int idx = 0;
            int step = 1;
            while ((step << 1) < (int)bit.size()) step <<= 1;
            for (; step > 0; step >>= 1) {
                int next = idx + step;
                if (next < (int)bit.size() && bit[next] < rank) {
                    idx = next;
                    rank -= bit[next];
                }
            }
            return vals[idx];
        };
        for (int x : nums) {
            add((int)(std::lower_bound(vals.begin(), vals.end(), x) - vals.begin()) + 1);
        }
        auto powm = [&](long long a, long long e) {
            long long res = 1;
            while (e > 0) {
                if (e & 1) res = res * a % mod;
                a = a * a % mod;
                e >>= 1;
            }
            return res;
        };
        std::vector<int> ans(queries.size());
        int size = (int)nums.size();
        long long cur = p;
        for (int i = 0; i < (int)queries.size(); i++) {
            add((int)(std::lower_bound(vals.begin(), vals.end(), queries[i][0]) - vals.begin()) + 1);
            size++;
            int x = kth(size - queries[i][1] + 1);
            cur = powm(cur, x);
            ans[i] = (int)cur;
        }
        return ans;
    }
};
