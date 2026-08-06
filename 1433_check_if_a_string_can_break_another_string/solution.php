<?php
class Solution {
    function checkIfCanBreak($s1, $s2) {
        $a = str_split($s1);
        $b = str_split($s2);
        sort($a);
        sort($b);
        $ge = true;
        $le = true;
        for ($i = 0; $i < count($a); $i++) {
            if ($a[$i] < $b[$i]) $ge = false;
            if ($a[$i] > $b[$i]) $le = false;
        }
        return $ge || $le;
    }
}
