// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

#include <climits>
#include <vector>
#include <algorithm>

class Solution {
public:
    int closestMeetingNode(std::vector<int>& edges, int node1, int node2) {
        int n = (int)edges.size();
        auto dist = [&](int start) {
            std::vector<int> d(n, -1);
            int cur = start, step = 0;
            while (cur != -1 && d[cur] == -1) {
                d[cur] = step;
                cur = edges[cur];
                step++;
            }
            return d;
        };
        auto d1 = dist(node1), d2 = dist(node2);
        int ans = -1, best = INT_MAX;
        for (int i = 0; i < n; i++) {
            if (d1[i] == -1 || d2[i] == -1) continue;
            int mx = std::max(d1[i], d2[i]);
            if (mx < best) {
                best = mx;
                ans = i;
            }
        }
        return ans;
    }
};
