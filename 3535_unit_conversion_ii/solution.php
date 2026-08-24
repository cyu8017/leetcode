<?php
// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

class Solution {
    private $MOD = 1000000007;
    private $g;
    private $res;

    private function qpow($x, $n) {
        $res = 1;
        $mod = $this->MOD;
        $x %= $mod;
        while ($n > 0) {
            if ($n & 1) $res = (int)(($res * $x) % $mod);
            $x = (int)(($x * $x) % $mod);
            $n >>= 1;
        }
        return $res;
    }

    private function dfs($s, $mul) {
        $this->res[$s] = $mul;
        foreach ($this->g[$s] as $e)
            $this->dfs($e[0], (int)(($mul * $e[1]) % $this->MOD));
    }

    function queryConversions($conversions, $queries) {
        $n = count($conversions) + 1;
        $this->g = array_fill(0, $n, []);
        foreach ($conversions as $e) $this->g[$e[0]][] = [$e[1], $e[2]];
        $this->res = array_fill(0, $n, 0);
        $this->dfs(0, 1);
        $ans = array_fill(0, count($queries), 0);
        for ($i = 0; $i < count($queries); $i++)
            $ans[$i] = (int)(($this->res[$queries[$i][1]] * $this->qpow($this->res[$queries[$i][0]], $this->MOD - 2)) % $this->MOD);
        return $ans;
    }
}
