<?php
// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

class Solution {
    /**
     * @param String $s
     * @param String $t
     * @return String
     */
    function minWindow($s, $t) {
        if ($t === "") {
            return "";
        }

        $need = [];
        $tLen = strlen($t);
        for ($i = 0; $i < $tLen; $i++) {
            $ch = $t[$i];
            if (!isset($need[$ch])) {
                $need[$ch] = 0;
            }
            $need[$ch]++;
        }

        $required = count($need);
        $formed = 0;
        $window = [];
        $left = 0;
        $sLen = strlen($s);
        $bestLen = PHP_INT_MAX;
        $bestLeft = 0;

        for ($right = 0; $right < $sLen; $right++) {
            $ch = $s[$right];
            if (!isset($window[$ch])) {
                $window[$ch] = 0;
            }
            $window[$ch]++;
            if (isset($need[$ch]) && $window[$ch] === $need[$ch]) {
                $formed++;
            }

            while ($formed === $required) {
                if ($right - $left + 1 < $bestLen) {
                    $bestLen = $right - $left + 1;
                    $bestLeft = $left;
                }

                $leftCh = $s[$left];
                $window[$leftCh]--;
                if (isset($need[$leftCh]) && $window[$leftCh] < $need[$leftCh]) {
                    $formed--;
                }
                $left++;
            }
        }

        if ($bestLen === PHP_INT_MAX) {
            return "";
        }

        return substr($s, $bestLeft, $bestLen);
    }
}
