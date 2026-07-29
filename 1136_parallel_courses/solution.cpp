// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

#include <queue>
#include <vector>

class Solution {
public:
    int minimumSemesters(int n, std::vector<std::vector<int>>& relations) {
        std::vector<std::vector<int>> graph(n + 1);
        std::vector<int> indegree(n + 1, 0);
        for (const auto& r : relations) {
            graph[r[0]].push_back(r[1]);
            ++indegree[r[1]];
        }
        std::queue<int> q;
        for (int i = 1; i <= n; ++i) if (indegree[i] == 0) q.push(i);
        int semesters = 0, taken = 0;
        while (!q.empty()) {
            ++semesters;
            int sz = static_cast<int>(q.size());
            for (int i = 0; i < sz; ++i) {
                int course = q.front(); q.pop();
                ++taken;
                for (int nxt : graph[course]) if (--indegree[nxt] == 0) q.push(nxt);
            }
        }
        return taken == n ? semesters : -1;
    }
};
