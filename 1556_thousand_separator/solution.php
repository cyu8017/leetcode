<?php

class Solution {
    /**
     * @param Integer $n
     * @return String
     */
    function thousandSeparator($n) {
        $s = (string)$n;
        $parts = [];
        while ($s !== '') {
            $parts[] = substr($s, -3);
            $s = substr($s, 0, max(0, strlen($s) - 3));
        }
        return implode('.', array_reverse($parts));
    }
}
