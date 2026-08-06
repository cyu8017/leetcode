<?php
class Solution {
    /**
     * @param Integer $n
     * @return Integer
     */
    function countTriples($n) {
        $squares = [];
        for ($i = 1; $i <= $n; $i++) {
            $squares[$i * $i] = true;
        }
        $ans = 0;
        for ($a = 1; $a <= $n; $a++) {
            for ($b = 1; $b <= $n; $b++) {
                if (isset($squares[$a * $a + $b * $b])) {
                    $ans++;
                }
            }
        }
        return $ans;
    }
}
