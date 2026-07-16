// LeetCode 0356 - Line Reflection

// https://leetcode.com/problems/line-reflection/



using System.Collections.Generic;



public class Solution {

    public bool IsReflected(int[][] points) {

        HashSet<string> pointSet = new();

        int minX = int.MaxValue;

        int maxX = int.MinValue;



        foreach (int[] point in points) {

            int x = point[0];

            int y = point[1];

            pointSet.Add($"{x},{y}");

            minX = Math.Min(minX, x);

            maxX = Math.Max(maxX, x);

        }



        int target = minX + maxX;

        foreach (int[] point in points) {

            int x = point[0];

            int y = point[1];

            if (!pointSet.Contains($"{target - x},{y}")) {

                return false;

            }

        }



        return true;

    }

}
