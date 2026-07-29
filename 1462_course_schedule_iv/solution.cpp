#include <vector>

class Solution {
public:
    std::vector<bool> checkIfPrerequisite(int numCourses, std::vector<std::vector<int>>& prerequisites,
                                          std::vector<std::vector<int>>& queries) {
        std::vector<std::vector<bool>> reach(numCourses, std::vector<bool>(numCourses, false));
        for (auto& e : prerequisites) reach[e[0]][e[1]] = true;
        for (int k = 0; k < numCourses; ++k)
            for (int i = 0; i < numCourses; ++i)
                if (reach[i][k])
                    for (int j = 0; j < numCourses; ++j)
                        reach[i][j] = reach[i][j] || reach[k][j];
        std::vector<bool> answer;
        for (auto& q : queries) answer.push_back(reach[q[0]][q[1]]);
        return answer;
    }
};
