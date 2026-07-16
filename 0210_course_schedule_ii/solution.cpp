// LeetCode 0210 - Course Schedule II
#include <queue>
#include <vector>
class Solution { public: std::vector<int> findOrder(int numCourses, std::vector<std::vector<int>>& prerequisites) { std::vector<std::vector<int>> graph(numCourses); std::vector<int> indegree(numCourses); for (const auto& edge : prerequisites) { graph[edge[1]].push_back(edge[0]); ++indegree[edge[0]]; } std::queue<int> queue; for (int i = 0; i < numCourses; ++i) if (!indegree[i]) queue.push(i); std::vector<int> order; while (!queue.empty()) { int course = queue.front(); queue.pop(); order.push_back(course); for (int next : graph[course]) if (--indegree[next] == 0) queue.push(next); } return order.size() == static_cast<size_t>(numCourses) ? order : std::vector<int>{}; } };
