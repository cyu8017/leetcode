<?php
// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution {
    private $nums;
    private $n;
    private $memo;
    const NEG = -1.0e18;

    function maximumTotalCost($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->memo = [];
        for ($i = 0; $i < $this->n; $i++) $this->memo[$i] = [self::NEG, self::NEG];
        return $this->dfs(0, 0);
    }

    private function dfs($i, $j) {
        if ($i >= $this->n) return 0;
        if ($this->memo[$i][$j] !== self::NEG) return $this->memo[$i][$j];
        $res = $this->nums[$i] + $this->dfs($i + 1, 1);
        if ($j > 0) $res = max($res, -$this->nums[$i] + $this->dfs($i + 1, 0));
        return $this->memo[$i][$j] = $res;
    }
}
