<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function closestToTarget($arr, $target) {
        $answer = PHP_INT_MAX;
        $current = [];
        foreach ($arr as $value) {
            $next = [$value => true];
            foreach ($current as $previous => $_) {
                $next[$value & $previous] = true;
            }
            $current = $next;
            foreach ($current as $candidate => $_) {
                $answer = min($answer, abs($candidate - $target));
            }
        }
        return $answer;
    }
}
