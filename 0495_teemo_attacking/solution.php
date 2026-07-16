<?php
// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

class Solution {
    /**
     * @param Integer[] $timeSeries
     * @param Integer $duration
     * @return Integer
     */
    function findPoisonedDuration($timeSeries, $duration) {
        return $this->find_poisoned_duration($timeSeries, $duration);
    }

    /**
     * @param Integer[] $timeSeries
     * @param Integer $duration
     * @return Integer
     */
    function find_poisoned_duration($timeSeries, $duration) {
        if ($timeSeries === []) {
            return 0;
        }
        $total = $duration;
        for ($index = 1; $index < count($timeSeries); $index++) {
            $total += min($duration, $timeSeries[$index] - $timeSeries[$index - 1]);
        }
        return $total;
    }
}
