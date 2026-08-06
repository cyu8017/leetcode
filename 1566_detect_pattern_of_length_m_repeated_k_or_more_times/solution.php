<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $m
     * @param Integer $k
     * @return Boolean
     */
    function containsPattern($arr, $m, $k) {
        $run = 0;
        for ($i = $m; $i < count($arr); $i++) {
            $run = $arr[$i] === $arr[$i - $m] ? $run + 1 : 0;
            if ($run >= $m * ($k - 1)) {
                return true;
            }
        }
        return false;
    }
}
