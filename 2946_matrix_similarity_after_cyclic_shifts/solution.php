<?php
// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution {
    function areSimilar($mat, $k) {
        $m = count($mat);
        $n = count($mat[0]);
        for ($i = 0; $i < $m; $i++) {
            if ($i % 2 === 0) {
                $shift = $n - ($k % $n);
                if ($shift === $n) $shift = 0;
            } else {
                $shift = $k % $n;
            }
            for ($j = 0; $j < $n; $j++) {
                if ($mat[$i][$j] !== $mat[$i][($j + $shift) % $n]) return false;
            }
        }
        return true;
    }
}
