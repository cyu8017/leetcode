// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

class Solution {
    private boolean knows(int a, int b, int[][] graph) {
        return graph[a][b] == 1;
    }

    public int findCelebrity(int[][] graph) {
        int n = graph.length;
        int candidate = 0;
        for (int person = 1; person < n; person++) {
            if (knows(candidate, person, graph)) {
                candidate = person;
            }
        }
        for (int person = 0; person < n; person++) {
            if (person == candidate) {
                continue;
            }
            if (knows(candidate, person, graph) || !knows(person, candidate, graph)) {
                return -1;
            }
        }
        return candidate;
    }
}
