// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

class Solution {
    public int maximumPopulation(int[][] logs) {
        int[] diff = new int[101];

        for (int[] log : logs) {
            diff[log[0] - 1950]++;
            diff[log[1] - 1950]--;
        }

        int bestYear = 1950;
        int bestPopulation = 0;
        int population = 0;

        for (int offset = 0; offset < 101; offset++) {
            population += diff[offset];
            if (population > bestPopulation) {
                bestPopulation = population;
                bestYear = 1950 + offset;
            }
        }

        return bestYear;
    }
}
