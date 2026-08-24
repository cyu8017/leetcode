<?php
// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

class Solution {
    function countPairs($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                if ($this->almostEqual($nums[$i], $nums[$j])) $ans++;
        return $ans;
    }

    private function almostEqual($a, $b) {
        $sa = (string)$a;
        $sb = (string)$b;
        while (strlen($sa) < strlen($sb)) $sa = '0' . $sa;
        while (strlen($sb) < strlen($sa)) $sb = '0' . $sb;
        $diff = [];
        $len = strlen($sa);
        for ($i = 0; $i < $len; $i++) if ($sa[$i] !== $sb[$i]) $diff[] = $i;
        if (count($diff) === 0) return true;
        if (count($diff) !== 2) return false;
        $i0 = $diff[0];
        $j = $diff[1];
        return $sa[$i0] === $sb[$j] && $sa[$j] === $sb[$i0];
    }
}
