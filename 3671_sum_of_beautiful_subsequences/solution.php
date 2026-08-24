<?php
// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

class Solution {
    function totalBeauty($nums) {
        $MOD = 1000000007;
        $mx = 0;
        foreach ($nums as $v) if ($v > $mx) $mx = $v;
        $pos = array_fill(0, $mx + 1, []);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) $pos[$nums[$i]][] = $i;
        $cnt = array_fill(0, $mx + 1, 0);
        for ($g = 1; $g <= $mx; $g++) {
            $seq = [];
            for ($m = $g; $m <= $mx; $m += $g)
                foreach ($pos[$m] as $p) $seq[] = $p;
            if (count($seq) === 0) continue;
            sort($seq);
            $ways = 1;
            for ($i = 0; $i < count($seq); $i++) $ways = ($ways * 2) % $MOD;
            $cnt[$g] = ($ways - 1 + $MOD) % $MOD;
        }
        $ans = 0;
        for ($g = $mx; $g >= 1; $g--) {
            for ($m = 2 * $g; $m <= $mx; $m += $g)
                $cnt[$g] = ($cnt[$g] - $cnt[$m] + $MOD) % $MOD;
            $ans = ($ans + $cnt[$g] * $g) % $MOD;
        }
        return $ans;
    }
}
