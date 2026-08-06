<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function findLengthOfShortestSubarray($arr) {
        $n = count($arr);
        $right = $n - 1;
        while ($right > 0 && $arr[$right - 1] <= $arr[$right]) {
            $right--;
        }
        if ($right === 0) {
            return 0;
        }
        $answer = $right;
        $left = 0;
        while ($left === 0 || ($left < $n && $arr[$left - 1] <= $arr[$left])) {
            while ($right < $n && $arr[$right] < $arr[$left]) {
                $right++;
            }
            $answer = min($answer, $right - $left - 1);
            $left++;
            if ($left >= $n) {
                break;
            }
        }
        return $answer;
    }
}
