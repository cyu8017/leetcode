// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

class Uniform {
    private static java.util.function.DoubleBinaryOperator uniformFn = (a, b) -> 0.0;
    private static Iterator<Double> sequence;

    static void setSequence(double[] values) {
        List<Double> items = new ArrayList<>();
        for (double value : values) {
            items.add(value);
        }
        sequence = items.iterator();
        uniformFn = (a, b) -> sequence.next();
    }

    static void set_uniform(java.util.function.DoubleBinaryOperator fn) {
        uniformFn = fn;
    }

    static void setUniform(java.util.function.DoubleBinaryOperator fn) {
        set_uniform(fn);
    }

    static double uniform(double a, double b) {
        return uniformFn.applyAsDouble(a, b);
    }
}

class Solution {
    private final int[] prefix;
    private final int total;

    public Solution(int[] w) {
        prefix = new int[w.length];
        int runningTotal = 0;
        for (int index = 0; index < w.length; index++) {
            runningTotal += w[index];
            prefix[index] = runningTotal;
        }
        total = runningTotal;
    }

    public int pickIndex() {
        int target = (int) Uniform.uniform(0, total);
        if (target >= total) {
            target = total - 1;
        }
        return bisectRight(prefix, target);
    }

    private int bisectRight(int[] values, int target) {
        int low = 0;
        int high = values.length - 1;
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
