// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

class Solution {
    public double getMinDistSum(int[][] positions) {
        double x = 0.0;
        double y = 0.0;
        for (int[] position : positions) {
            x += position[0];
            y += position[1];
        }
        x /= positions.length;
        y /= positions.length;

        for (int iter = 0; iter < 10000; iter++) {
            double numeratorX = 0.0;
            double numeratorY = 0.0;
            double denominator = 0.0;
            double[] coincident = null;

            for (int[] position : positions) {
                double px = position[0];
                double py = position[1];
                double d = Math.hypot(x - px, y - py);
                if (d < 1e-12) {
                    coincident = new double[] { px, py };
                    break;
                }
                numeratorX += px / d;
                numeratorY += py / d;
                denominator += 1.0 / d;
            }

            double nx;
            double ny;
            if (coincident != null) {
                nx = coincident[0];
                ny = coincident[1];
            } else {
                nx = numeratorX / denominator;
                ny = numeratorY / denominator;
            }

            if (Math.hypot(nx - x, ny - y) < 1e-8) {
                x = nx;
                y = ny;
                break;
            }
            x = nx;
            y = ny;
        }

        double total = 0.0;
        for (int[] position : positions) {
            total += Math.hypot(x - position[0], y - position[1]);
        }
        return total;
    }
}
