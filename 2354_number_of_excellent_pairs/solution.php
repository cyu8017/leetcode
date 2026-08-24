<?php
// LeetCode 2354 - Number of Excellent Pairs
// https://leetcode.com/problems/number-of-excellent-pairs/

class Solution {
    function countExcellentPairs($nums, $k) {
        $uniq = [];
        foreach ($nums as $x) $uniq[$x] = true;
        $cnt = array_fill(0, 32, 0);
        foreach ($uniq as $x => $_) $cnt[$this->bitCount($x)]++;
        $ans = 0;
        for ($i = 0; $i < 32; $i++) {
            for ($j = 0; $j < 32; $j++) {
                if ($i + $j >= $k) $ans += $cnt[$i] * $cnt[$j];
            }
        }
        return $ans;
    }

    private function bitCount($x) {
        $c = 0;
        while ($x) { $x &= $x - 1; $c++; }
        return $c;
    }
}
