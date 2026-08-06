<?php
class Solution {
    function kthFactor($n, $k) {
        for ($x = 1; $x <= $n; $x++) {
            if ($n % $x === 0) {
                $k--;
                if ($k === 0) return $x;
            }
        }
        return -1;
    }
}
