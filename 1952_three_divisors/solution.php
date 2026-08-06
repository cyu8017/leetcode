<?php
class Solution {
    /**
     * @param Integer $n
     * @return Boolean
     */
    function isThree($n) {
        $root = (int)sqrt($n);
        if ($root * $root != $n || $root < 2) {
            return false;
        }
        $i = 2;
        while ($i * $i <= $root) {
            if ($root % $i == 0) {
                return false;
            }
            $i++;
        }
        return true;
    }
}
