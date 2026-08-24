<?php
// LeetCode 3149 - Find the Minimum Cost Array Permutation
// https://leetcode.com/problems/find-the-minimum-cost-array-permutation/

class Solution {
    public $nums;
    public $n;
    public $memo;
    public $ans;
    function findPermutation($nums) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->memo = [];
        for ($i = 0; $i < (1 << $this->n); $i++) $this->memo[] = array_fill(0, $this->n, -1);
        $this->ans = [];
        $this->g(1, 0);
        return $this->ans;
    }
    function absv($x) { return $x < 0 ? -$x : $x; }
    function dfs($mask, $pre) {
        $n = $this->n;
        $nums = $this->nums;
        if ($mask === (1 << $n) - 1) return $this->absv($pre - $nums[0]);
        if ($this->memo[$mask][$pre] !== -1) return $this->memo[$mask][$pre];
        $res = PHP_INT_MAX;
        for ($cur = 1; $cur < $n; $cur++) {
            if ((($mask >> $cur) & 1) === 0) {
                $res = min($res, $this->absv($pre - $nums[$cur]) + $this->dfs($mask | (1 << $cur), $cur));
            }
        }
        return $this->memo[$mask][$pre] = $res;
    }
    function g($mask, $pre) {
        $this->ans[] = $pre;
        $n = $this->n;
        $nums = $this->nums;
        if ($mask === (1 << $n) - 1) return;
        $res = $this->dfs($mask, $pre);
        for ($cur = 1; $cur < $n; $cur++) {
            if ((($mask >> $cur) & 1) === 0) {
                if ($this->absv($pre - $nums[$cur]) + $this->dfs($mask | (1 << $cur), $cur) === $res) {
                    $this->g($mask | (1 << $cur), $cur);
                    break;
                }
            }
        }
    }
}
