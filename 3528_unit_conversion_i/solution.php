<?php
// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

class Solution {
    private $g;
    private $ans;
    private $mod = 1000000007;

    private function dfs($s, $mul) {
        $this->ans[$s] = $mul;
        foreach ($this->g[$s] as $e)
            $this->dfs($e[0], (int)(($mul * $e[1]) % $this->mod));
    }

    function baseUnitConversions($conversions) {
        $n = count($conversions) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($conversions as $e) $this->g[$e[0]][] = [$e[1], $e[2]];
        $this->ans = array_fill(0, $n, 0);
        $this->dfs(0, 1);
        return $this->ans;
    }
}
