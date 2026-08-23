// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

using System.Collections.Generic;

public class Excel {
    private readonly int height;
    private readonly int width;
    private readonly int[][] values;
    private readonly Dictionary<(int, int), List<(int, int)>> formulas = new();

    public Excel(int height, char width) {
        this.height = height;
        this.width = width - 'A' + 1;
        values = new int[height + 1][];
        for (int i = 0; i <= height; ++i) values[i] = new int[this.width];
    }

    private (int, int) Parse(string cell) {
        return (int.Parse(cell.Substring(1)), cell[0] - 'A');
    }

    private int Eval(int row, int col) {
        var key = (row, col);
        if (formulas.TryGetValue(key, out var cells)) {
            int total = 0;
            foreach (var (r, c) in cells) total += Eval(r, c);
            return total;
        }
        return values[row][col];
    }

    public void Set(int row, char column, int val) {
        int col = column - 'A';
        formulas.Remove((row, col));
        values[row][col] = val;
    }

    public int Get(int row, char column) => Eval(row, column - 'A');

    public int Sum(int row, char column, string[] numbers) {
        int col = column - 'A';
        var cells = new List<(int, int)>();
        foreach (string token in numbers) {
            int colon = token.IndexOf(':');
            if (colon >= 0) {
                var (r1, c1) = Parse(token.Substring(0, colon));
                var (r2, c2) = Parse(token.Substring(colon + 1));
                for (int r = r1; r <= r2; ++r)
                    for (int c = c1; c <= c2; ++c)
                        cells.Add((r, c));
            } else {
                cells.Add(Parse(token));
            }
        }
        formulas[(row, col)] = cells;
        return Eval(row, col);
    }
}
