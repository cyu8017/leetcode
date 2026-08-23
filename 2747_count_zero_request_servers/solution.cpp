// LeetCode 2747 - Count Zero Request Servers
// https://leetcode.com/problems/count-zero-request-servers/

#include <vector>
#include <algorithm>
#include <unordered_map>

class Solution {
public:
    std::vector<int> countServers(int n, std::vector<std::vector<int>>& logs, int x, std::vector<int>& queries) {
        std::sort(logs.begin(), logs.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
        struct Qi { int t, i; };
        std::vector<Qi> qs(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) qs[i] = {queries[i], i};
        std::sort(qs.begin(), qs.end(), [](auto& a, auto& b) { return a.t < b.t; });
        std::vector<int> ans(queries.size());
        std::unordered_map<int, int> cnt;
        int active = 0, l = 0, r = 0;
        for (auto& q : qs) {
            while (r < (int)logs.size() && logs[r][1] <= q.t) {
                int id = logs[r][0];
                if (cnt[id] == 0) active++;
                cnt[id]++;
                r++;
            }
            while (l < r && logs[l][1] < q.t - x) {
                int id = logs[l][0];
                cnt[id]--;
                if (cnt[id] == 0) active--;
                l++;
            }
            ans[q.i] = n - active;
        }
        return ans;
    }
};
