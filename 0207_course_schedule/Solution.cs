// LeetCode 0207 - Course Schedule\n// https://leetcode.com/problems/\n\nusing System.Collections.Generic;

public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        var graph = new List<int>[numCourses];
        for (var i = 0; i < numCourses; i++) graph[i] = new List<int>();
        var indegree = new int[numCourses];
        foreach (var pair in prerequisites) { graph[pair[1]].Add(pair[0]); indegree[pair[0]]++; }
        var queue = new Queue<int>();
        for (var i = 0; i < numCourses; i++) if (indegree[i] == 0) queue.Enqueue(i);
        var taken = 0;
        while (queue.Count > 0) {
            var course = queue.Dequeue(); taken++;
            foreach (var next in graph[course]) if (--indegree[next] == 0) queue.Enqueue(next);
        }
        return taken == numCourses;
    }
}
