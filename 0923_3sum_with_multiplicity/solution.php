<?php
// LeetCode 0923 - 3Sum With Multiplicity
// https://leetcode.com/problems/3sum-with-multiplicity/

class Solution {
    function threeSumMulti($arr, $target) {
        $MOD = 1000000007;
        $count = array_fill(0, 101, 0);
        foreach ($arr as $x) $count[$x]++;
        $ans = 0;
        for ($a = 0; $a <= 100; $a++) if ($count[$a] > 0) {
            for ($b = $a; $b <= 100; $b++) if ($count[$b] > 0) {
                $c = $target - $a - $b;
                if ($c < $b || $c > 100 || $count[$c] === 0) continue;
                if ($a === $b && $b === $c) $ans += intdiv($count[$a] * ($count[$a] - 1) * ($count[$a] - 2), 6);
                elseif ($a === $b) $ans += intdiv($count[$a] * ($count[$a] - 1), 2) * $count[$c];
                elseif ($b === $c) $ans += $count[$a] * intdiv($count[$b] * ($count[$b] - 1), 2);
                else $ans += $count[$a] * $count[$b] * $count[$c];
            }
        }
        return $ans % $MOD;
    }
}
