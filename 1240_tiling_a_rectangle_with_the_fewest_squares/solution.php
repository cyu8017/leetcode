<?php
// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

class Solution {
    private $heights;
    private $best;
    private $n;
    private $m;

    /**
     * @param Integer $n
     * @param Integer $m
     * @return Integer
     */
    function tilingRectangle($n, $m) {
        if ($n > $m) [$n, $m] = [$m, $n];
        $this->n = $n;
        $this->m = $m;
        $this->heights = array_fill(0, $m, 0);
        $this->best = $n * $m;
        $this->search(0);
        return $this->best;
    }

    private function search($used) {
        if ($used >= $this->best) return;
        $low = min($this->heights);
        if ($low === $this->n) {
            $this->best = $used;
            return;
        }
        $left = array_search($low, $this->heights, true);
        $right = $left;
        while ($right < $this->m && $this->heights[$right] === $low) $right++;
        $maxSize = min($this->n - $low, $right - $left);
        for ($size = $maxSize; $size >= 1; $size--) {
            for ($i = $left; $i < $left + $size; $i++) $this->heights[$i] = $low + $size;
            $this->search($used + 1);
            for ($i = $left; $i < $left + $size; $i++) $this->heights[$i] = $low;
        }
    }
}
