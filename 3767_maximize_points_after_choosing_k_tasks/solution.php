<?php
// LeetCode 3767 - Maximize Points After Choosing K Tasks
// https://leetcode.com/problems/maximize-points-after-choosing-k-tasks/

class Solution {
    function maxPoints($technique1, $technique2, $k) {
        $n = count($technique1);
        $idx = range(0, $n - 1);
        usort($idx, function($i, $j) use ($technique1, $technique2) {
            return ($technique1[$j] - $technique2[$j]) <=> ($technique1[$i] - $technique2[$i]);
        });
        $ans = 0;
        foreach ($technique2 as $x) $ans += $x;
        for ($i = 0; $i < $k; $i++) {
            $index = $idx[$i];
            $ans -= $technique2[$index];
            $ans += $technique1[$index];
        }
        for ($i = $k; $i < $n; $i++) {
            $index = $idx[$i];
            if ($technique1[$index] >= $technique2[$index]) {
                $ans -= $technique2[$index];
                $ans += $technique1[$index];
            }
        }
        return $ans;
    }
}
