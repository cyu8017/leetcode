// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

#include <algorithm>
#include <set>
#include <string>
#include <vector>

class Solution {
public:
    int minOperations(std::string s, int k) {
        int n = (int)s.size();
        std::set<int> ts[2];
        for (int i = 0; i <= n; i++) ts[i % 2].insert(i);
        int cnt0 = (int)std::count(s.begin(), s.end(), '0');
        ts[cnt0 % 2].erase(cnt0);
        std::vector<int> q{cnt0};
        int ans = 0;
        while (!q.empty()) {
            std::vector<int> nq;
            for (int cur : q) {
                if (cur == 0) return ans;
                int l = cur + k - 2 * std::min(cur, k);
                int r = cur + k - 2 * std::max(k - n + cur, 0);
                auto& t = ts[l % 2];
                auto it = t.lower_bound(l);
                while (it != t.end() && *it <= r) {
                    nq.push_back(*it);
                    it = t.erase(it);
                }
            }
            q = std::move(nq);
            ans++;
        }
        return -1;
    }
};
