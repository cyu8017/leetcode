// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

using System.Collections.Generic;

public class Solution {
    public int MinimumSemesters(int n, int[][] relations) {
        var graph = new List<int>[n + 1];
        for (int i = 0; i <= n; i++) graph[i] = new List<int>();
        int[] indegree = new int[n + 1];
        foreach (var r in relations) {
            graph[r[0]].Add(r[1]);
            indegree[r[1]]++;
        }
        var q = new Queue<int>();
        for (int i = 1; i <= n; i++) if (indegree[i] == 0) q.Enqueue(i);
        int semesters = 0, taken = 0;
        while (q.Count > 0) {
            semesters++;
            int sz = q.Count;
            for (int i = 0; i < sz; i++) {
                int course = q.Dequeue();
                taken++;
                foreach (int nxt in graph[course]) {
                    if (--indegree[nxt] == 0) q.Enqueue(nxt);
                }
            }
        }
        return taken == n ? semesters : -1;
    }
}
