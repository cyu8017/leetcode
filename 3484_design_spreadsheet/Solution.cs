// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

using System.Collections.Generic;

public class Spreadsheet {
    readonly Dictionary<string, int> cells = new();

    public Spreadsheet(int rows) { }

    public void SetCell(string cell, int value) { cells[cell] = value; }

    public void ResetCell(string cell) { cells.Remove(cell); }

    public int GetValue(string formula) {
        if (formula.Length > 0 && formula[0] == '=') formula = formula.Substring(1);
        int sum = 0;
        int start = 0;
        while (start < formula.Length) {
            int plus = formula.IndexOf('+', start);
            string p = plus < 0 ? formula.Substring(start) : formula.Substring(start, plus - start);
            bool isNum = p.Length > 0 && (char.IsDigit(p[0]) || (p[0] == '-' && p.Length > 1));
            if (isNum) {
                for (int i = 1; i < p.Length; i++) if (!char.IsDigit(p[i])) { isNum = false; break; }
            }
            if (isNum) sum += int.Parse(p);
            else {
                cells.TryGetValue(p, out int v);
                sum += v;
            }
            if (plus < 0) break;
            start = plus + 1;
        }
        return sum;
    }
}
