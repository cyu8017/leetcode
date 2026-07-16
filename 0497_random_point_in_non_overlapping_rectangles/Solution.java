// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

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
    private final int[][] rects;
    private final int total;

    public Solution(int[][] rects) {
        this.rects = rects;
        int areaTotal = 0;
        for (int[] rect : rects) {
            int width = rect[2] - rect[0] + 1;
            int height = rect[3] - rect[1] + 1;
            areaTotal += width * height;
        }
        this.total = areaTotal;
    }

    public int[] pick() {
        int index = (int) Uniform.uniform(0, total);
        if (index >= total) {
            index = total - 1;
        }
        for (int[] rect : rects) {
            int width = rect[2] - rect[0] + 1;
            int height = rect[3] - rect[1] + 1;
            int size = width * height;
            if (index < size) {
                int offsetX = index % width;
                int offsetY = index / width;
                return new int[] { rect[0] + offsetX, rect[1] + offsetY };
            }
            index -= size;
        }
        int[] last = rects[rects.length - 1];
        return new int[] { last[0], last[1] };
    }
}
