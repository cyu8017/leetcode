<?php
// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

class Solution {
    function lexSmallest($s) {
        $ans = $s;
        $n = strlen($s);
        $reverse = function(&$a, $l, $r) {
            for ($i = $l, $j = $r - 1; $i < $j; $i++, $j--) {
                $t = $a[$i]; $a[$i] = $a[$j]; $a[$j] = $t;
            }
        };
        for ($k = 1; $k <= $n; $k++) {
            $a1 = str_split($s);
            $reverse($a1, 0, $k);
            $t1 = implode('', $a1);
            $a2 = str_split($s);
            $reverse($a2, $n - $k, $n);
            $t2 = implode('', $a2);
            if ($t1 < $ans) $ans = $t1;
            if ($t2 < $ans) $ans = $t2;
        }
        return $ans;
    }
}
