// LeetCode 3935 - Power Update After K Th Largest Insertion I
// https://leetcode.com/problems/power-update-after-k-th-largest-insertion-i/

#include <map>
#include <vector>

class Solution {
    static void merge(std::map<int, int>& st, int x, int v) {
        int c = st.count(x) ? st[x] : 0;
        if (c + v == 0) st.erase(x);
        else st[x] = c + v;
    }

public:
    std::vector<int> powerUpdate(std::vector<int>& nums, int p, std::vector<std::vector<int>>& queries) {
        std::map<int, int> L, R;
        int sz1 = 0, sz2 = (int)nums.size();
        for (int x : nums) merge(R, x, 1);
        const int mod = 1000000007;
        auto qpow = [&](long long a, int b) {
            long long ans = 1;
            while (b > 0) {
                if (b & 1) ans = ans * a % mod;
                a = a * a % mod;
                b >>= 1;
            }
            return (int)ans;
        };
        std::vector<int> ans;
        ans.reserve(queries.size());
        for (auto& q : queries) {
            int val = q[0], k = q[1];
            merge(R, val, 1);
            sz2++;
            int node = R.begin()->first;
            merge(R, node, -1);
            sz2--;
            merge(L, node, 1);
            sz1++;
            while (sz2 < k) {
                node = L.rbegin()->first;
                merge(L, node, -1);
                sz1--;
                merge(R, node, 1);
                sz2++;
            }
            while (sz2 > k) {
                node = R.begin()->first;
                merge(R, node, -1);
                sz2--;
                merge(L, node, 1);
                sz1++;
            }
            int x = R.begin()->first;
            p = qpow(p, x);
            ans.push_back(p);
        }
        return ans;
    }
};
