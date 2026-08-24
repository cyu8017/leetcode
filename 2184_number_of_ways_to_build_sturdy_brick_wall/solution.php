<?php
// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

class Solution {
    private $masks = [];
    private $bricks;

    private function gen($remain, $mask) {
        if ($remain === 0) {
            $this->masks[] = $mask;
            return;
        }
        foreach ($this->bricks as $b) {
            if ($b <= $remain) {
                $nm = $mask;
                if ($remain - $b > 0) $nm |= 1 << ($remain - $b);
                $this->gen($remain - $b, $nm);
            }
        }
    }

    /**
     * @param Integer $height
     * @param Integer $width
     * @param Integer[] $bricks
     * @return Integer
     */
    function buildWall($height, $width, $bricks) {
        $MOD = 1000000007;
        $this->bricks = $bricks;
        $this->masks = [];
        $this->gen($width, 0);
        $m = count($this->masks);
        $compat = array_fill(0, $m, []);
        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $m; $j++)
                if (($this->masks[$i] & $this->masks[$j]) === 0) $compat[$i][] = $j;
        }
        $dp = array_fill(0, $m, 1);
        for ($h = 1; $h < $height; $h++) {
            $ndp = array_fill(0, $m, 0);
            for ($i = 0; $i < $m; $i++)
                foreach ($compat[$i] as $j) $ndp[$j] = ($ndp[$j] + $dp[$i]) % $MOD;
            $dp = $ndp;
        }
        $ans = 0;
        foreach ($dp as $v) $ans = ($ans + $v) % $MOD;
        return $ans;
    }
}
