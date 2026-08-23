// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> queryResults(int limit, std::vector<std::vector<int>>& queries) {
        std::unordered_map<int, int> g, cnt;
        std::vector<int> ans;
        for (auto& q : queries) {
            int x = q[0], y = q[1];
            cnt[y]++;
            auto it = g.find(x);
            if (it != g.end()) {
                if (--cnt[it->second] == 0) cnt.erase(it->second);
            }
            g[x] = y;
            ans.push_back((int)cnt.size());
        }
        return ans;
    }
};
