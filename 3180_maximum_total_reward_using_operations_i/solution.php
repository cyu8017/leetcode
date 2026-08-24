<?php
// LeetCode 3180 - Maximum Total Reward Using Operations I
// https://leetcode.com/problems/maximum-total-reward-using-operations-i/

class Solution {
    private $rewardValues;
    private $f;
    private $n;

    function maxTotalReward($rewardValues) {
        sort($rewardValues);
        $this->rewardValues = $rewardValues;
        $this->n = count($rewardValues);
        $this->f = array_fill(0, $rewardValues[$this->n - 1] << 1, -1);
        return $this->dfs(0);
    }

    private function upperBound($x) {
        $lo = 0;
        $hi = $this->n;
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($this->rewardValues[$mid] <= $x) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }

    private function dfs($x) {
        if ($this->f[$x] !== -1) return $this->f[$x];
        $idx = $this->upperBound($x);
        $this->f[$x] = 0;
        for ($it = $idx; $it < $this->n; $it++) {
            $this->f[$x] = max($this->f[$x], $this->rewardValues[$it] + $this->dfs($x + $this->rewardValues[$it]));
        }
        return $this->f[$x];
    }
}
