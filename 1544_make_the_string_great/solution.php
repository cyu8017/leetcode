<?php

class Solution {
    /**
     * @param String $s
     * @return String
     */
    function makeGood($s) {
        $stack = [];
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $ch = $s[$i];
            if (!empty($stack)) {
                $top = $stack[count($stack) - 1];
                if ($top !== $ch && strtolower($top) === strtolower($ch)) {
                    array_pop($stack);
                    continue;
                }
            }
            $stack[] = $ch;
        }
        return implode('', $stack);
    }
}
