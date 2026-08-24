<?php
// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution {
    function robotWithString($s) {
        $n = strlen($s);
        $minSuf = array_fill(0, $n + 1, '');
        $minSuf[$n] = chr(ord('z') + 1);
        for ($i = $n - 1; $i >= 0; $i--)
            $minSuf[$i] = $s[$i] < $minSuf[$i + 1] ? $s[$i] : $minSuf[$i + 1];
        $stack = [];
        $ans = [];
        for ($i = 0; $i < $n; $i++) {
            $stack[] = $s[$i];
            while (count($stack) && $stack[count($stack) - 1] <= $minSuf[$i + 1])
                $ans[] = array_pop($stack);
        }
        while (count($stack)) $ans[] = array_pop($stack);
        return implode('', $ans);
    }
}
