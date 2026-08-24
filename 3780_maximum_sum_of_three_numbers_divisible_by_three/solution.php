<?php
// LeetCode 3780 - Maximum Sum of Three Numbers Divisible by Three
// https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/

class Solution {
    function maximumSum($nums) {
        $a = $nums;
        sort($a);
        $g = [[], [], []];
        foreach ($a as $x) $g[$x % 3][] = $x;
        $ans = 0;
        for ($aa = 0; $aa < 3; $aa++) {
            if (count($g[$aa])) {
                $x = array_pop($g[$aa]);
                for ($b = 0; $b < 3; $b++) {
                    if (count($g[$b])) {
                        $y = array_pop($g[$b]);
                        $c = (3 - ($aa + $b) % 3) % 3;
                        if (count($g[$c])) {
                            $z = $g[$c][count($g[$c]) - 1];
                            $ans = max($ans, $x + $y + $z);
                        }
                        $g[$b][] = $y;
                    }
                }
                $g[$aa][] = $x;
            }
        }
        return $ans;
    }
}
