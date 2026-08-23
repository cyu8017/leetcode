// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

#include <vector>

class Solution {
public:
    std::vector<int> shortestDistanceAfterQueries(int n, std::vector<std::vector<int>>& queries) {
        std::vector<int> nxt(n - 1);
        for (int i = 0; i < n - 1; i++) nxt[i] = i + 1;
        int cnt = n - 1;
        std::vector<int> ans;
        for (auto& q : queries) {
            int u = q[0], v = q[1];
            if (nxt[u] > 0 && nxt[u] < v) {
                int i = nxt[u];
                while (i < v) {
                    cnt--;
                    int ni = nxt[i];
                    nxt[i] = 0;
                    i = ni;
                }
                nxt[u] = v;
            }
            ans.push_back(cnt);
        }
        return ans;
    }
};
