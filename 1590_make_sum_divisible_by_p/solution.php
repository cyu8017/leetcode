<?php

class Solution {
    /**
     * @param Integer[] $nums
     * @param Integer $p
     * @return Integer
     */
    function minSubarray($nums, $p) {
        $target = array_sum($nums) % $p;
        if ($target === 0) {
            return 0;
        }
        $seen = [0 => -1];
        $prefix = 0;
        $answer = count($nums);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            $prefix = ($prefix + $nums[$i]) % $p;
            $need = ($prefix - $target + $p) % $p;
            if (array_key_exists($need, $seen)) {
                $answer = min($answer, $i - $seen[$need]);
            }
            $seen[$prefix] = $i;
        }
        return $answer < $n ? $answer : -1;
    }
}
