// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class Uniform {
    private static Iterator<Double> sequence;

    static void setSequence(double[] values) {
        List<Double> items = new ArrayList<>();
        for (double value : values) {
            items.add(value);
        }
        sequence = items.iterator();
    }

    static double uniform(double a, double b) {
        return sequence.next();
    }
}

class Solution {
    private final double radius;
    private final double xCenter;
    private final double yCenter;

    public Solution(double radius, double xCenter, double yCenter) {
        this.radius = radius;
        this.xCenter = xCenter;
        this.yCenter = yCenter;
    }

    public double[] randPoint() {
        while (true) {
            double x = Uniform.uniform(-radius, radius);
            double y = Uniform.uniform(-radius, radius);
            if (x * x + y * y <= radius * radius) {
                return new double[] {
                    Math.round((xCenter + x) * 100000.0) / 100000.0,
                    Math.round((yCenter + y) * 100000.0) / 100000.0,
                };
            }
        }
    }
}
