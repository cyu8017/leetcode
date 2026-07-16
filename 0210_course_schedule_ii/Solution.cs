// LeetCode 0210 - Course Schedule II\n// https://leetcode.com/problems/\n\nusing System.Collections.Generic;

public class Solution {
    public int[] FindOrder(int numCourses, int[][] prerequisites) {
        var graph = new List<int>[numCourses];
        for (var i = 0; i < numCourses; i++) graph[i] = new List<int>();
        var indegree = new int[numCourses];
        foreach (var pair in prerequisites) { graph[pair[1]].Add(pair[0]); indegree[pair[0]]++; }
        var queue = new Queue<int>();
        for (var i = 0; i < numCourses; i++) if (indegree[i] == 0) queue.Enqueue(i);
        var order = new int[numCourses]; var index = 0;
        while (queue.Count > 0) {
            var course = queue.Dequeue(); order[index++] = course;
            foreach (var next in graph[course]) if (--indegree[next] == 0) queue.Enqueue(next);
        }
        return index == numCourses ? order : new int[0];
    }
}
