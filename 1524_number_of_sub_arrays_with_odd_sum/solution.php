<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numOfSubarrays($arr) {
        $counts = [1, 0];
        $parity = 0;
        $answer = 0;
        foreach ($arr as $value) {
            $parity ^= $value & 1;
            $answer += $counts[$parity ^ 1];
            $counts[$parity]++;
        }
        return $answer % 1000000007;
    }
}
