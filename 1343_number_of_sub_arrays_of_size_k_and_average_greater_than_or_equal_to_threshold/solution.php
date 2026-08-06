<?php
class Solution {
    function numOfSubarrays($arr, $k, $threshold) {
        $window = array_sum(array_slice($arr, 0, $k));
        $answer = $window >= $k * $threshold ? 1 : 0;
        for ($i = $k; $i < count($arr); $i++) {
            $window += $arr[$i] - $arr[$i - $k];
            if ($window >= $k * $threshold) $answer++;
        }
        return $answer;
    }
}
