<?php

class Solution {
    /**
     * @param String $s
     * @return Integer
     */
    function minInsertions($s) {
        $insertions = 0;
        $needed = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            if ($s[$i] === '(') {
                $needed += 2;
                if ($needed & 1) {
                    $insertions++;
                    $needed--;
                }
            } else {
                $needed--;
                if ($needed < 0) {
                    $insertions++;
                    $needed = 1;
                }
            }
        }
        return $insertions + $needed;
    }
}
