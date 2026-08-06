<?php

class Solution {
    /**
     * @param Integer $n
     * @param Integer $k
     * @return String
     */
    function findKthBit($n, $k) {
        $invert = false;
        $length = (1 << $n) - 1;
        while ($k !== 1) {
            $middle = intdiv($length, 2) + 1;
            if ($k === $middle) {
                return $invert ? '0' : '1';
            }
            if ($k > $middle) {
                $k = $length - $k + 1;
                $invert = !$invert;
            }
            $length = intdiv($length, 2);
        }
        return $invert ? '1' : '0';
    }
}
