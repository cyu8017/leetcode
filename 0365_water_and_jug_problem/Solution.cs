// LeetCode 0365 - Water and Jug Problem

// https://leetcode.com/problems/water-and-jug-problem/



public class Solution {

    public bool CanMeasureWater(int x, int y, int target) {

        if (target == 0) {

            return true;

        }

        if (x + y < target) {

            return false;

        }

        return target % Gcd(x, y) == 0;

    }



    private static int Gcd(int a, int b) {

        while (b != 0) {

            int temp = b;

            b = a % b;

            a = temp;

        }

        return a;

    }

}
