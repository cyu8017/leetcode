<?php
// LeetCode 3863 - Minimum Operations to Sort a String
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/

class Solution {
    function minOperations($s) {
        $n = strlen($s);
        $sorted = true;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] < $s[$i - 1]) { $sorted = false; break; }
        }
        if ($sorted) return 0;
        if ($n === 2) return -1;
        $mn = $s[0];
        $mx = $s[0];
        for ($i = 0; $i < $n; $i++) {
            $c = $s[$i];
            if ($c < $mn) $mn = $c;
            if ($c > $mx) $mx = $c;
        }
        if ($s[0] === $mn || $s[$n - 1] === $mx) return 1;
        for ($i = 1; $i < $n - 1; $i++) {
            if ($s[$i] === $mn || $s[$i] === $mx) return 2;
        }
        return 3;
    }
}
