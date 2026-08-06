<?php
class Solution {
    function countTriplets($arr) {
        $answer = 0;
        $n = count($arr);
        for ($i = 0; $i < $n; $i++) {
            $value = 0;
            for ($k = $i; $k < $n; $k++) {
                $value ^= $arr[$k];
                if ($value === 0) $answer += $k - $i;
            }
        }
        return $answer;
    }
}
