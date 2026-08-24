<?php
// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

class Solution {
    private $nums;
    private $limit;
    private $memo;
    private $MIN;

    function maxProduct($nums, $k, $limit) {
        $this->nums = $nums;
        $this->limit = $limit;
        $this->MIN = -5000;
        $this->memo = [];
        $sumAll = 0;
        foreach ($nums as $v) $sumAll += $v;
        if (abs($k) > $sumAll) return -1;
        $ans = $this->dp(0, 1, 0, $k);
        return $ans === $this->MIN ? -1 : $ans;
    }

    private function dp($i, $product, $state, $kk) {
        $n = count($this->nums);
        if ($i === $n) {
            if ($kk === 0 && $state !== 0 && $product <= $this->limit) return $product;
            return $this->MIN;
        }
        $key = $i . ',' . $product . ',' . $state . ',' . $kk;
        if (isset($this->memo[$key])) return $this->memo[$key];
        $res = $this->dp($i + 1, $product, $state, $kk);
        if ($state === 0) $res = max($res, $this->dp($i + 1, $this->nums[$i], 1, $kk - $this->nums[$i]));
        if ($state === 1) {
            $np = $product * $this->nums[$i];
            if ($np > $this->limit + 1) $np = $this->limit + 1;
            $res = max($res, $this->dp($i + 1, $np, 2, $kk + $this->nums[$i]));
        }
        if ($state === 2) {
            $np = $product * $this->nums[$i];
            if ($np > $this->limit + 1) $np = $this->limit + 1;
            $res = max($res, $this->dp($i + 1, $np, 1, $kk - $this->nums[$i]));
        }
        return $this->memo[$key] = $res;
    }
}
