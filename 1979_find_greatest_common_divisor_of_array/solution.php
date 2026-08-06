<?php
class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findGCD($nums) {
        $a = min($nums);
        $b = max($nums);
        while ($b !== 0) {
            $t = $b;
            $b = $a % $b;
            $a = $t;
        }
        return $a;
    }
}
