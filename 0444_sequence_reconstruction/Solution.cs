// LeetCode 0444 - Sequence Reconstruction
// https://leetcode.com/problems/sequence-reconstruction/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool SequenceReconstruction(int[] nums, IList<IList<int>> sequences) {
        Dictionary<int, int> indegree = nums.ToDictionary(value => value, _ => 0);
        Dictionary<int, HashSet<int>> graph = nums.ToDictionary(value => value, _ => new HashSet<int>());
        HashSet<(int, int)> seenEdges = new HashSet<(int, int)>();

        foreach (IList<int> sequence in sequences) {
            for (int index = 0; index < sequence.Count - 1; index++) {
                int left = sequence[index];
                int right = sequence[index + 1];
                if (!seenEdges.Add((left, right))) {
                    continue;
                }
                graph[left].Add(right);
                indegree[right]++;
            }
        }

        Queue<int> queue = new Queue<int>(nums.Where(value => indegree[value] == 0));
        List<int> order = new List<int>();
        while (queue.Count > 0) {
            if (queue.Count > 1) {
                return false;
            }
            int node = queue.Dequeue();
            order.Add(node);
            foreach (int neighbor in graph[node]) {
                indegree[neighbor]--;
                if (indegree[neighbor] == 0) {
                    queue.Enqueue(neighbor);
                }
            }
        }

        return order.SequenceEqual(nums);
    }
}
