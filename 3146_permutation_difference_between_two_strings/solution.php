<?php
// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution {
    function findPermutationDifference($s, $t) {
        $d = array_fill(0, 26, 0);
        $n = strlen($s);
        for ($i = 0; $i < $n; $i++) $d[ord($s[$i]) - 97] = $i;
        $ans = 0;
        $nt = strlen($t);
        for ($i = 0; $i < $nt; $i++) $ans += abs($d[ord($t[$i]) - 97] - $i);
        return $ans;
    }
}
