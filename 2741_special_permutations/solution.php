<?php
// LeetCode 2741 - Special Permutations
// https://leetcode.com/problems/special-permutations/

class Solution {
    public $nums;
    public $memo;
    public $n;
    function specialPerm($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->memo = array_fill(0, 1 << $this->n, array_fill(0, $this->n, -1));
        $ans = 0;
        for ($i = 0; $i < $this->n; $i++) $ans = ($ans + $this->dfs(1 << $i, $i)) % 1000000007;
        return $ans;
    }
    function dfs($mask, $last) {
        $MOD = 1000000007;
        if ($mask === (1 << $this->n) - 1) return 1;
        if ($this->memo[$mask][$last] !== -1) return $this->memo[$mask][$last];
        $res = 0;
        for ($i = 0; $i < $this->n; $i++) {
            if ($mask & (1 << $i)) continue;
            if ($this->nums[$i] % $this->nums[$last] === 0 || $this->nums[$last] % $this->nums[$i] === 0)
                $res = ($res + $this->dfs($mask | (1 << $i), $i)) % $MOD;
        }
        return $this->memo[$mask][$last] = $res;
    }
}
