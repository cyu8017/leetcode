// LeetCode 1237 - Find Positive Integer Solution for a Given Equation
// https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

using System.Collections.Generic;

public class CustomFunction {
    public virtual int F(int x, int y) => 0;
}

public class Solution {
    public IList<IList<int>> FindSolution(CustomFunction customfunction, int z) {
        var answer = new List<IList<int>>();
        int x = 1, y = 1000;
        while (x <= 1000 && y >= 1) {
            int value = customfunction.F(x, y);
            if (value == z) {
                answer.Add(new int[] { x, y });
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
