// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

static class Uniform {
    private static Queue<double>? sequence;

    public static void SetSequence(double[] values) {
        sequence = new Queue<double>(values);
    }

    public static double Uniform(double a, double b) {
        return sequence!.Dequeue();
    }
}

public class Solution {
    private readonly int[][] rects;
    private readonly int total;

    public Solution(int[][] rects) {
        this.rects = rects;
        int areaTotal = 0;
        foreach (int[] rect in rects) {
            int width = rect[2] - rect[0] + 1;
            int height = rect[3] - rect[1] + 1;
            areaTotal += width * height;
        }
        total = areaTotal;
    }

    public int[] Pick() {
        int index = (int)Uniform.Uniform(0, total);
        if (index >= total) {
            index = total - 1;
        }
        foreach (int[] rect in rects) {
            int width = rect[2] - rect[0] + 1;
            int height = rect[3] - rect[1] + 1;
            int size = width * height;
            if (index < size) {
                int offsetX = index % width;
                int offsetY = index / width;
                return new[] { rect[0] + offsetX, rect[1] + offsetY };
            }
            index -= size;
        }
        int[] last = rects[^1];
        return new[] { last[0], last[1] };
    }
}
