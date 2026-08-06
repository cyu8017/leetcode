<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $m
     * @return Integer
     */
    function findLatestStep($arr, $m) {
        if ($m === count($arr)) {
            return $m;
        }
        $lengths = [];
        $answer = -1;
        foreach ($arr as $step => $x) {
            $step++;
            $left = $lengths[$x - 1] ?? 0;
            $right = $lengths[$x + 1] ?? 0;
            $size = $left + 1 + $right;
            $lengths[$x - $left] = $size;
            $lengths[$x + $right] = $size;
            if ($left === $m || $right === $m) {
                $answer = $step - 1;
            }
        }
        return $answer;
    }
}
