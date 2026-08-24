<?php
// LeetCode 2712 - Minimum Cost to Make All Characters Equal
// https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/

class Solution {
    function minimumCost($s) {
        $n = strlen($s);
        $ans = 0;
        for ($i = 1; $i < $n; $i++) {
            if ($s[$i] !== $s[$i - 1]) $ans += min($i, $n - $i);
        }
        return $ans;
    }
}
