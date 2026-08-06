<?php

class Solution {
    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function getLucky($s, $k) {
        $num = '';
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $num .= (ord($s[$i]) - 96);
        }
        for ($t = 0; $t < $k; $t++) {
            $sum = 0;
            $nlen = strlen($num);
            for ($i = 0; $i < $nlen; $i++) {
                $sum += (int)$num[$i];
            }
            $num = (string)$sum;
        }
        return (int)$num;
    }
}
