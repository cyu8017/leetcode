<?php
// LeetCode 0335 - Self Crossing
// https://leetcode.com/problems/self-crossing/

class Solution {
    /**
     * @param Integer[] $distance
     * @return Boolean
     */
    function isSelfCrossing($distance) {
        return $this->is_self_crossing($distance);
    }

    /**
     * @param Integer[] $distance
     * @return Boolean
     */
    function is_self_crossing($distance) {
        $count = count($distance);
        for ($index = 3; $index < $count; $index++) {
            if ($distance[$index] >= $distance[$index - 2] && $distance[$index - 1] <= $distance[$index - 3]) {
                return true;
            }
            if ($index >= 4 && $distance[$index - 1] === $distance[$index - 3]) {
                if ($distance[$index - 2] >= $distance[$index - 4] + $distance[$index]) {
                    return true;
                }
            }
            if ($index >= 5) {
                if ($distance[$index - 4] >= $distance[$index - 2] - $distance[$index]) {
                    if ($distance[$index] >= $distance[$index - 2] - $distance[$index - 4]) {
                        if ($distance[$index - 1] <= $distance[$index - 3]) {
                            if ($distance[$index - 5] + $distance[$index - 1] >= $distance[$index - 3]) {
                                return true;
                            }
                        }
                    }
                }
            }
        }
        return false;
    }
}
