<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function threeConsecutiveOdds($arr) {
        $run = 0;
        foreach ($arr as $value) {
            $run = ($value & 1) ? $run + 1 : 0;
            if ($run === 3) {
                return true;
            }
        }
        return false;
    }
}
