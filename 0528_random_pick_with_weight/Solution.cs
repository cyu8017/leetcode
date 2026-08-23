// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

static class Uniform {
    private static Func<double, double, double> uniformFn = (_, _) => 0.0;
    private static Queue<double>? sequence;

    public static void SetSequence(double[] values) {
        sequence = new Queue<double>(values);
        uniformFn = (_, _) => sequence!.Dequeue();
    }

    public static void set_uniform(Func<double, double, double> fn) {
        uniformFn = fn;
    }

    public static void SetUniform(Func<double, double, double> fn) {
        uniformFn = fn;
    }

    public static double Uniform(double a, double b) {
        return uniformFn(a, b);
    }
}

public class Solution {
    private readonly int[] prefix;
    private readonly int total;

    public Solution(int[] w) {
        prefix = new int[w.Length];
        int runningTotal = 0;
        for (int index = 0; index < w.Length; index++) {
            runningTotal += w[index];
            prefix[index] = runningTotal;
        }
        total = runningTotal;
    }

    public int PickIndex() {
        int target = (int)Uniform.Uniform(0, total);
        if (target >= total) {
            target = total - 1;
        }
        return BisectRight(prefix, target);
    }

    private static int BisectRight(int[] values, int target) {
        int low = 0;
        int high = values.Length - 1;
        while (low < high) {
            int mid = (low + high) / 2;
            if (values[mid] <= target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}
