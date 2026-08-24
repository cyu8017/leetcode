<?php
// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

class Solution {
    /**
     * @param String $s
     * @return String[]
     */
    function ambiguousCoordinates($s) {
        $digits = substr($s, 1, strlen($s) - 2);
        $candidates = function($frag) {
            $options = [];
            $len = strlen($frag);
            if ($len === 0 || ($len > 1 && $frag[0] === '0' && $frag[$len - 1] === '0')) return $options;
            if ($frag[0] === '0' && $len > 1) {
                if ($frag[$len - 1] !== '0') $options[] = "0." . substr($frag, 1);
                return $options;
            }
            $options[] = $frag;
            if ($frag[$len - 1] === '0') return $options;
            for ($i = 1; $i < $len; $i++) {
                $options[] = substr($frag, 0, $i) . "." . substr($frag, $i);
            }
            return $options;
        };
        $answer = [];
        $n = strlen($digits);
        for ($i = 1; $i < $n; $i++) {
            foreach ($candidates(substr($digits, 0, $i)) as $left) {
                foreach ($candidates(substr($digits, $i)) as $right) {
                    $answer[] = "(" . $left . ", " . $right . ")";
                }
            }
        }
        return $answer;
    }
}
