<?php
// LeetCode 1854 - Maximum Population Year
// https://leetcode.com/problems/maximum-population-year/

class Solution {
    /**
     * @param Integer[][] $logs
     * @return Integer
     */
    function maximumPopulation($logs) {
        $diff = array_fill(0, 101, 0);

        foreach ($logs as [$birth, $death]) {
            $diff[$birth - 1950]++;
            $diff[$death - 1950]--;
        }

        $bestYear = 1950;
        $bestPopulation = 0;
        $population = 0;

        for ($offset = 0; $offset < 101; $offset++) {
            $population += $diff[$offset];
            if ($population > $bestPopulation) {
                $bestPopulation = $population;
                $bestYear = 1950 + $offset;
            }
        }

        return $bestYear;
    }
}
