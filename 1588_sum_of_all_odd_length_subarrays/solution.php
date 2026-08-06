<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function sumOddLengthSubarrays($arr) {
        $n = count($arr);
        $answer = 0;
        for ($i = 0; $i < $n; $i++) {
            $answer += $arr[$i] * intdiv(($i + 1) * ($n - $i) + 1, 2);
        }
        return $answer;
    }
}
