// LeetCode 0370 - Range Addition

// https://leetcode.com/problems/range-addition/



public class Solution {

    public int[] GetModifiedArray(int length, int[][] updates) {

        int[] diff = new int[length + 1];



        foreach (int[] update in updates) {

            int start = update[0];

            int end = update[1];

            int inc = update[2];

            diff[start] += inc;

            if (end + 1 < diff.Length) {

                diff[end + 1] -= inc;

            }

        }



        int[] result = new int[length];

        int running = 0;

        for (int index = 0; index < length; index++) {

            running += diff[index];

            result[index] = running;

        }

        return result;

    }

}
