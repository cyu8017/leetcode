// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

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
    private final int cols;
    private final int total;
    private List<Integer> available;

    public Solution(int m, int n) {
        this.cols = n;
        this.total = m * n;
        reset();
    }

    public int[] flip() {
        int index = (int) Uniform.uniform(0, available.size() - 1);
        if (index >= available.size()) {
            index = available.size() - 1;
        }
        int value = available.get(index);
        available.set(index, available.get(available.size() - 1));
        available.remove(available.size() - 1);
        return new int[] { value / cols, value % cols };
    }

    public void reset() {
        available = new ArrayList<>();
        for (int index = 0; index < total; index++) {
            available.add(index);
        }
    }
}
