// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

import java.util.*;

class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int startNode, int endNode) {
        List<List<double[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            int a = edges[i][0];
            int b = edges[i][1];
            double probability = succProb[i];
            graph.get(a).add(new double[] { b, probability });
            graph.get(b).add(new double[] { a, probability });
        }

        PriorityQueue<double[]> heap = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        double[] best = new double[n];
        best[startNode] = 1.0;
        heap.offer(new double[] { 1.0, startNode });

        while (!heap.isEmpty()) {
            double[] current = heap.poll();
            double probability = current[0];
            int node = (int) current[1];
            if (node == endNode) {
                return probability;
            }
            if (probability < best[node]) {
                continue;
            }
            for (double[] edge : graph.get(node)) {
                int neighbor = (int) edge[0];
                double edgeProbability = edge[1];
                double candidate = probability * edgeProbability;
                if (candidate > best[neighbor]) {
                    best[neighbor] = candidate;
                    heap.offer(new double[] { candidate, neighbor });
                }
            }
        }
        return 0.0;
    }
}
