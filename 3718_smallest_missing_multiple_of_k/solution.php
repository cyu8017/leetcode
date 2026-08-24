<?php
// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution {
    function missingMultiple($nums, $k) {
        $s = [];
        foreach ($nums as $x) $s[$x] = true;
        for ($i = 1; ; $i++) {
            $x = $k * $i;
            if (!isset($s[$x])) return $x;
        }
    }
}
