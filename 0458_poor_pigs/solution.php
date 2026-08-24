<?php
// LeetCode 0458 - Poor Pigs
// https://leetcode.com/problems/poor-pigs/

class Solution {
    /**
     * @param int $buckets
     * @param int $minutesToDie
     * @param int $minutesToTest
     * @return int
     */
    function poorPigs($buckets, $minutesToDie, $minutesToTest) {
        return $this->poor_pigs($buckets, $minutesToDie, $minutesToTest);
    }

    /**
     * @param int $buckets
     * @param int $minutesToDie
     * @param int $minutesToTest
     * @return int
     */
    function poor_pigs($buckets, $minutesToDie, $minutesToTest) {
        $states = intdiv($minutesToTest, $minutesToDie) + 1;
        $pigs = 0;
        $capacity = 1;
        while ($capacity < $buckets) {
            $pigs++;
            $capacity *= $states;
        }
        return $pigs;
    }
}
