// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

import java.util.*;

class Solution {
    public int minimumSemesters(int n, int[][] relations) {
        List<Integer>[] graph = new List[n + 1];
        for (int i = 1; i <= n; i++) graph[i] = new ArrayList<>();
        int[] indegree = new int[n + 1];
        for (int[] e : relations) {
            graph[e[0]].add(e[1]);
            indegree[e[1]]++;
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= n; i++) if (indegree[i] == 0) queue.offer(i);
        int semesters = 0, taken = 0;
        while (!queue.isEmpty()) {
            semesters++;
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int course = queue.poll();
                taken++;
                for (int nxt : graph[course]) {
                    if (--indegree[nxt] == 0) queue.offer(nxt);
                }
            }
        }
        return taken == n ? semesters : -1;
    }
}
