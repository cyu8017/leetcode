// LeetCode 1462 - Course Schedule Iv
// https://leetcode.com/problems/course-schedule-iv/

using System.Collections.Generic;
public class Solution {
    public IList<bool> CheckIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        var reach = new bool[numCourses, numCourses];
        foreach (var e in prerequisites) reach[e[0], e[1]] = true;
        for (int k = 0; k < numCourses; k++)
            for (int i = 0; i < numCourses; i++)
                if (reach[i, k])
                    for (int j = 0; j < numCourses; j++)
                        reach[i, j] |= reach[k, j];
        var answer = new List<bool>();
        foreach (var q in queries) answer.Add(reach[q[0], q[1]]);
        return answer;
    }
}
