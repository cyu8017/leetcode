// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

import java.util.PriorityQueue;

class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<double[]> heap =
            new PriorityQueue<>((x, y) -> Double.compare(y[0], x[0]));
        for (int[] cls : classes) {
            double p = cls[0];
            double t = cls[1];
            heap.offer(new double[] { gain(p, t), p, t });
        }
        for (int i = 0; i < extraStudents; i++) {
            double[] top = heap.poll();
            double p = top[1] + 1;
            double t = top[2] + 1;
            heap.offer(new double[] { gain(p, t), p, t });
        }
        double total = 0;
        for (double[] entry : heap) {
            total += entry[1] / entry[2];
        }
        return total / classes.length;
    }

    private double gain(double p, double t) {
        return (p + 1) / (t + 1) - p / t;
    }
}
