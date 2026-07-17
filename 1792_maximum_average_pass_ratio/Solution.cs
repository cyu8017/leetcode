// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

public class Solution {
    public double MaxAverageRatio(int[][] classes, int extraStudents) {
        static double Gain(double p, double t) => (p + 1) / (t + 1) - p / t;

        var heap = new PriorityQueue<(double p, double t), double>();
        foreach (var cls in classes) {
            double p = cls[0];
            double t = cls[1];
            heap.Enqueue((p, t), -Gain(p, t));
        }
        for (int i = 0; i < extraStudents; i++) {
            var (p, t) = heap.Dequeue();
            p += 1;
            t += 1;
            heap.Enqueue((p, t), -Gain(p, t));
        }
        double total = 0;
        while (heap.Count > 0) {
            var (p, t) = heap.Dequeue();
            total += p / t;
        }
        return total / classes.Length;
    }
}
