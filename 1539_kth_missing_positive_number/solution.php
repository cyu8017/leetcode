<?php

class Solution {
    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Integer
     */
    function findKthPositive($arr, $k) {
        $left = 0;
        $right = count($arr);
        while ($left < $right) {
            $middle = intdiv($left + $right, 2);
            if ($arr[$middle] - $middle - 1 < $k) {
                $left = $middle + 1;
            } else {
                $right = $middle;
            }
        }
        return $left + $k;
    }
}
