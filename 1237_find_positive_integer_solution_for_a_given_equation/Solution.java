// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

import java.util.*;

class CustomFunction {
    public int f(int x, int y) {
        return 0;
    }
}

class Solution {
    public List<List<Integer>> findSolution(CustomFunction customfunction, int z) {
        List<List<Integer>> answer = new ArrayList<>();
        int x = 1, y = 1000;
        while (x <= 1000 && y >= 1) {
            int value = customfunction.f(x, y);
            if (value == z) {
                answer.add(Arrays.asList(x, y));
                x++;
                y--;
            } else if (value < z) {
                x++;
            } else {
                y--;
            }
        }
        return answer;
    }
}

