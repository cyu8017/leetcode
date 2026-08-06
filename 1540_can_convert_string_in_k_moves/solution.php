<?php

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @param Integer $k
     * @return Boolean
     */
    function canConvertString($s, $t, $k) {
        if (strlen($s) !== strlen($t)) {
            return false;
        }
        $used = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $shift = (ord($t[$i]) - ord($s[$i]) + 26) % 26;
            if ($shift !== 0) {
                $used[$shift]++;
                if ($shift + 26 * ($used[$shift] - 1) > $k) {
                    return false;
                }
            }
        }
        return true;
    }
}
