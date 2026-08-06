<?php

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return Boolean
     */
    function isTransformable($s, $t) {
        $positions = array_fill(0, 10, []);
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $positions[(int)$s[$i]][] = $i;
        }
        $heads = array_fill(0, 10, 0);
        $tLen = strlen($t);
        for ($i = 0; $i < $tLen; $i++) {
            $d = (int)$t[$i];
            if ($heads[$d] >= count($positions[$d])) {
                return false;
            }
            $index = $positions[$d][$heads[$d]];
            for ($smaller = 0; $smaller < $d; $smaller++) {
                if ($heads[$smaller] < count($positions[$smaller])
                    && $positions[$smaller][$heads[$smaller]] < $index) {
                    return false;
                }
            }
            $heads[$d]++;
        }
        return true;
    }
}
