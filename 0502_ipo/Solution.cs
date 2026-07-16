// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

public class Solution {
    public int FindMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        (int Capital, int Profit)[] projects = capital
            .Select((value, index) => (value, profits[index]))
            .OrderBy(project => project.value)
            .ToArray();
        PriorityQueue<int, int> available = new(Comparer<int>.Create((left, right) => right.CompareTo(left)));
        int projectIndex = 0;
        for (int round = 0; round < k; round++) {
            while (projectIndex < projects.Length && projects[projectIndex].Capital <= w) {
                available.Enqueue(projects[projectIndex].Profit, projects[projectIndex].Profit);
                projectIndex++;
            }
            if (available.Count == 0) {
                break;
            }
            w += available.Dequeue();
        }
        return w;
    }
}
