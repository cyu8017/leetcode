// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

import java.util.HashMap;
import java.util.Map;

class Spreadsheet {
    private final Map<String, Integer> cells = new HashMap<>();

    public Spreadsheet(int rows) {}

    public void setCell(String cell, int value) { cells.put(cell, value); }

    public void resetCell(String cell) { cells.remove(cell); }

    public int getValue(String formula) {
        if (!formula.isEmpty() && formula.charAt(0) == '=') formula = formula.substring(1);
        int sum = 0;
        int start = 0;
        while (start < formula.length()) {
            int plus = formula.indexOf('+', start);
            String p = plus < 0 ? formula.substring(start) : formula.substring(start, plus);
            boolean isNum = !p.isEmpty() && (Character.isDigit(p.charAt(0)) || (p.charAt(0) == '-' && p.length() > 1));
            if (isNum) {
                for (int i = 1; i < p.length(); i++) if (!Character.isDigit(p.charAt(i))) { isNum = false; break; }
            }
            if (isNum) sum += Integer.parseInt(p);
            else sum += cells.getOrDefault(p, 0);
            if (plus < 0) break;
            start = plus + 1;
        }
        return sum;
    }
}
