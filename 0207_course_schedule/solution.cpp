// LeetCode 0207 - Course Schedule
#include <queue>
#include <vector>
class Solution { public: bool canFinish(int numCourses, std::vector<std::vector<int>>& prerequisites) { std::vector<std::vector<int>> graph(numCourses); std::vector<int> indegree(numCourses); for (const auto& edge : prerequisites) { graph[edge[1]].push_back(edge[0]); ++indegree[edge[0]]; } std::queue<int> queue; for (int i = 0; i < numCourses; ++i) if (!indegree[i]) queue.push(i); int taken = 0; while (!queue.empty()) { int course = queue.front(); queue.pop(); ++taken; for (int next : graph[course]) if (--indegree[next] == 0) queue.push(next); } return taken == numCourses; } };
