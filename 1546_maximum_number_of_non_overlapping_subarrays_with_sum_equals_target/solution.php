<?php

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $target
     * @return Integer
     */
    function maxNonOverlapping($nums, $target) {
        $seen = [0 => true];
        $prefix = 0;
        $answer = 0;
        foreach ($nums as $value) {
            $prefix += $value;
            if (isset($seen[$prefix - $target])) {
                $answer++;
                $prefix = 0;
                $seen = [0 => true];
            } else {
                $seen[$prefix] = true;
            }
        }
        return $answer;
    }
}
