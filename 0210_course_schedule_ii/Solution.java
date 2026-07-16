// LeetCode 0210 - Course Schedule II\n// https://leetcode.com/problems/\n\nimport java.util.ArrayList;
import java.util.ArrayDeque;
import java.util.List;
import java.util.Queue;

class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < numCourses; i++) graph.add(new ArrayList<>());
        int[] indegree = new int[numCourses];
        for (int[] pair : prerequisites) { graph.get(pair[1]).add(pair[0]); indegree[pair[0]]++; }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 0; i < numCourses; i++) if (indegree[i] == 0) queue.offer(i);
        int[] order = new int[numCourses];
        int index = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            order[index++] = course;
            for (int next : graph.get(course)) if (--indegree[next] == 0) queue.offer(next);
        }
        return index == numCourses ? order : new int[0];
    }
}
