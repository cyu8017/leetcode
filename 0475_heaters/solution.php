<?php
// LeetCode 0475 - Heaters
// https://leetcode.com/problems/heaters/

class Solution {
    /**
     * @param int[] $houses
     * @param int[] $heaters
     * @return int
     */
    function findRadius($houses, $heaters) {
        return $this->find_radius($houses, $heaters);
    }

    /**
     * @param int[] $houses
     * @param int[] $heaters
     * @return int
     */
    function find_radius($houses, $heaters) {
        sort($heaters);
        $radius = 0;
        foreach ($houses as $house) {
            $position = $this->bisectLeft($heaters, $house);
            $distances = [];
            if ($position < count($heaters)) {
                $distances[] = abs($heaters[$position] - $house);
            }
            if ($position > 0) {
                $distances[] = abs($heaters[$position - 1] - $house);
            }
            $radius = max($radius, min($distances));
        }
        return $radius;
    }

    /**
     * @param int[] $array
     * @param int $target
     * @return int
     */
    private function bisectLeft($array, $target) {
        $left = 0;
        $right = count($array);
        while ($left < $right) {
            $mid = intdiv($left + $right, 2);
            if ($array[$mid] < $target) {
                $left = $mid + 1;
            } else {
                $right = $mid;
            }
        }
        return $left;
    }
}
