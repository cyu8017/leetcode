<?php
// LeetCode 0370 - Range Addition
// https://leetcode.com/problems/range-addition/

class Solution {
    /**
     * @param Integer $length
     * @param Integer[][] $updates
     * @return Integer[]
     */
    function getModifiedArray($length, $updates) {
        return $this->get_modified_array($length, $updates);
    }

    /**
     * @param Integer $length
     * @param Integer[][] $updates
     * @return Integer[]
     */
    function get_modified_array($length, $updates) {
        $diff = array_fill(0, $length + 1, 0);

        foreach ($updates as $update) {
            [$start, $end, $inc] = $update;
            $diff[$start] += $inc;
            if ($end + 1 < count($diff)) {
                $diff[$end + 1] -= $inc;
            }
        }

        $result = array_fill(0, $length, 0);
        $running = 0;
        for ($index = 0; $index < $length; $index++) {
            $running += $diff[$index];
            $result[$index] = $running;
        }

        return $result;
    }
}
