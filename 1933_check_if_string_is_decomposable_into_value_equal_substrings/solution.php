<?php
class Solution {
    /**
     * @param String $s
     * @return Boolean
     */
    function isDecomposable($s) {
        $n = strlen($s);
        $i = 0;
        $twos = 0;
        while ($i < $n) {
            $j = $i;
            while ($j < $n && $s[$j] === $s[$i]) {
                $j++;
            }
            $length = $j - $i;
            if ($length % 3 === 1) {
                return false;
            }
            if ($length % 3 === 2) {
                $twos++;
                if ($twos > 1) {
                    return false;
                }
            }
            $i = $j;
        }
        return $twos === 1;
    }
}
