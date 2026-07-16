<?php

class Solution {
    function minCut($s) {
        $n = strlen($s);
        if ($n === 0) {
            return 0;
        }

        $isPalindrome = array_fill(0, $n, array_fill(0, $n, false));
        for ($start = $n - 1; $start >= 0; $start--) {
            for ($end = $start; $end < $n; $end++) {
                if ($s[$start] === $s[$end] &&
                    ($end - $start < 2 || $isPalindrome[$start + 1][$end - 1])) {
                    $isPalindrome[$start][$end] = true;
                }
            }
        }

        $cuts = range(0, $n - 1);
        for ($end = 0; $end < $n; $end++) {
            if ($isPalindrome[0][$end]) {
                $cuts[$end] = 0;
            } else {
                for ($start = 0; $start < $end; $start++) {
                    if ($isPalindrome[$start + 1][$end]) {
                        $cuts[$end] = min($cuts[$end], $cuts[$start] + 1);
                    }
                }
            }
        }
        return $cuts[$n - 1];
    }
}