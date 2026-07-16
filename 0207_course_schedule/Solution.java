// LeetCode 0207 - Course Schedule\n// https://leetcode.com/problems/\n\nimport java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.List;
import java.util.Queue;

class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] pair : prerequisites) { graph.get(pair[1]).add(pair[0]); indegree[pair[0]]++; }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) if (indegree[i] == 0) queue.offer(i);
        int taken = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            taken++;
            for (int next : graph.get(course)) if (--indegree[next] == 0) queue.offer(next);
        }
        return taken == numCourses;
    }
}
