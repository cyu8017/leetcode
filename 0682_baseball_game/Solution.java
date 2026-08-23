// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

import java.util.*;

class Solution {
    public int calPoints(String[] operations) {
        List<Integer> stack = new ArrayList<>();
        for (String op : operations) {
            if (op.equals("C")) stack.remove(stack.size() - 1);
            else if (op.equals("D")) stack.add(stack.get(stack.size() - 1) * 2);
            else if (op.equals("+")) stack.add(stack.get(stack.size() - 1) + stack.get(stack.size() - 2));
            else stack.add(Integer.parseInt(op));
        }
        int total = 0;
        for (int value : stack) total += value;
        return total;
    }
}
