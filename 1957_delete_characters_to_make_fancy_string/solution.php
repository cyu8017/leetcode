<?php
class Solution {
    /**
     * @param String $s
     * @return String
     */
    function makeFancyString($s) {
        $ans = [];
        $len = strlen($s);
        for ($i = 0; $i < $len; $i++) {
            $c = $s[$i];
            $n = count($ans);
            if ($n >= 2 && $ans[$n - 1] === $c && $ans[$n - 2] === $c) {
                continue;
            }
            $ans[] = $c;
        }
        return implode('', $ans);
    }
}
