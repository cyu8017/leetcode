// LeetCode 0356 - Line Reflection

// https://leetcode.com/problems/line-reflection/



import java.util.HashSet;

import java.util.Set;



class Solution {

    public boolean isReflected(int[][] points) {

        Set<String> pointSet = new HashSet<>();

        int minX = Integer.MAX_VALUE;

        int maxX = Integer.MIN_VALUE;



        for (int[] point : points) {

            int x = point[0];

            int y = point[1];

            pointSet.add(x + "," + y);

            minX = Math.min(minX, x);

            maxX = Math.max(maxX, x);

        }



        int target = minX + maxX;

        for (int[] point : points) {

            int x = point[0];

            int y = point[1];

            if (!pointSet.contains((target - x) + "," + y)) {

                return false;

            }

        }



        return true;

    }

}
