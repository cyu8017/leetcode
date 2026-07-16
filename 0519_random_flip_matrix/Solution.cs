// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

using System;
using System.Collections.Generic;

static class Uniform {
    private static Func<double, double, double> uniformFn = (a, b) => a;
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
    private readonly int cols;
    private readonly int total;
    private List<int> available;

    public Solution(int m, int n) {
        cols = n;
        total = m * n;
        available = new List<int>();
        Reset();
    }

    public int[] Flip() {
        int index = (int)Uniform.Uniform(0, available.Count - 1);
        if (index >= available.Count) {
            index = available.Count - 1;
        }
        int value = available[index];
        available[index] = available[^1];
        available.RemoveAt(available.Count - 1);
        return new[] { value / cols, value % cols };
    }

    public void Reset() {
        available = new List<int>(total);
        for (int index = 0; index < total; index++) {
            available.Add(index);
        }
    }
}
