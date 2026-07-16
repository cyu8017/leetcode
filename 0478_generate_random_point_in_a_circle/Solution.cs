// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

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
    private readonly double radius;
    private readonly double xCenter;
    private readonly double yCenter;

    public Solution(double radius, double xCenter, double yCenter) {
        this.radius = radius;
        this.xCenter = xCenter;
        this.yCenter = yCenter;
    }

    public double[] RandPoint() {
        while (true) {
            double x = Uniform.Uniform(-radius, radius);
            double y = Uniform.Uniform(-radius, radius);
            if (x * x + y * y <= radius * radius) {
                return new[] {
                    Math.Round(xCenter + x, 5),
                    Math.Round(yCenter + y, 5),
                };
            }
        }
    }
}
