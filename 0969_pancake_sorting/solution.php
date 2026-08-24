<?php
// LeetCode 0969 - Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

class Solution {
    function pancakeSort($arr) {
        $a = $arr;
        $ans = [];
        $indexOf = function ($v) use (&$a) {
            $n = count($a);
            for ($i = 0; $i < $n; $i++) if ($a[$i] === $v) return $i;
            return -1;
        };
        $reverse = function ($l, $r) use (&$a) {
            while ($l < $r) {
                $t = $a[$l]; $a[$l] = $a[$r]; $a[$r] = $t;
                $l++; $r--;
            }
        };
        for ($size = count($a); $size > 1; $size--) {
            $i = $indexOf($size);
            if ($i === $size - 1) continue;
            if ($i > 0) {
                $ans[] = $i + 1;
                $reverse(0, $i);
            }
            $ans[] = $size;
            $reverse(0, $size - 1);
        }
        return $ans;
    }
}
