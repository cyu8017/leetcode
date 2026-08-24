<?php
// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

class Solution {
    function processStr($s, $k) {
        $m = 0;
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c === '*') $m = $m > 0 ? $m - 1 : 0;
            else if ($c === '#') $m <<= 1;
            else if ($c !== '%') $m += 1;
        }
        $k2 = $k;
        if ($k2 >= $m) return '.';
        for ($i = $n - 1; ; $i--) {
            $c = $s[$i];
            if ($c === '*') $m += 1;
            else if ($c === '#') {
                $m = intdiv($m, 2);
                if ($k2 >= $m) $k2 -= $m;
            } else if ($c === '%') {
                $k2 = $m - 1 - $k2;
            } else {
                $m -= 1;
                if ($k2 === $m) return $c;
            }
        }
    }
}
