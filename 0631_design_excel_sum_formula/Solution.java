// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Excel {
    private final int[][] values;
    private final Map<Long, List<int[]>> formulas = new HashMap<>();

    public Excel(int height, char width) {
        values = new int[height + 1][width - 'A' + 1];
    }

    public void set(int row, char column, int val) {
        int col = column - 'A';
        formulas.remove(key(row, col));
        values[row][col] = val;
    }

    public int get(int row, char column) {
        return eval(row, column - 'A');
    }

    public int sum(int row, char column, String[] numbers) {
        int col = column - 'A';
        List<int[]> cells = new ArrayList<>();
        for (String token : numbers) {
            int colon = token.indexOf(':');
            if (colon >= 0) {
                int[] p1 = parse(token.substring(0, colon));
                int[] p2 = parse(token.substring(colon + 1));
                for (int r = p1[0]; r <= p2[0]; ++r) {
                    for (int c = p1[1]; c <= p2[1]; ++c) {
                        cells.add(new int[] {r, c});
                    }
                }
            } else {
                cells.add(parse(token));
            }
        }
        formulas.put(key(row, col), cells);
        return eval(row, col);
    }

    private int[] parse(String cell) {
        return new int[] {Integer.parseInt(cell.substring(1)), cell.charAt(0) - 'A'};
    }

    private int eval(int row, int col) {
        List<int[]> formula = formulas.get(key(row, col));
        if (formula != null) {
            int total = 0;
            for (int[] cell : formula) {
                total += eval(cell[0], cell[1]);
            }
            return total;
        }
        return values[row][col];
    }

    private long key(int row, int col) {
        return (((long) row) << 32) | (col & 0xffffffffL);
    }
}
