// LeetCode 0277 - Find the Celebrity
// https://leetcode.com/problems/find-the-celebrity/

public class Solution {
    private bool Knows(int a, int b, int[][] graph) {
        return graph[a][b] == 1;
    }

    public int FindCelebrity(int[][] graph) {
        int n = graph.Length;
        int candidate = 0;
        for (int person = 1; person < n; person++) {
            if (Knows(candidate, person, graph)) {
                candidate = person;
            }
        }
        for (int person = 0; person < n; person++) {
            if (person == candidate) {
                continue;
            }
            if (Knows(candidate, person, graph) || !Knows(person, candidate, graph)) {
                return -1;
            }
        }
        return candidate;
    }
}
