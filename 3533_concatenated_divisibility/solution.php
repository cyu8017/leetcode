<?php
// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

class Solution {
    private $nums;
    private $k;
    private $n;
    private $pows;
    private $memo;

    private function dp($mask, $mod) {
        if ($mask === (1 << $this->n) - 1) return $mod === 0;
        $key = $mask . ',' . $mod;
        if (isset($this->memo[$key])) return $this->memo[$key];
        for ($i = 0; $i < $this->n; $i++) {
            if ((($mask >> $i) & 1) === 0) {
                $nm = ($mod * $this->pows[$i] + $this->nums[$i]) % $this->k;
                if ($this->dp($mask | (1 << $i), $nm)) {
                    return $this->memo[$key] = true;
                }
            }
        }
        return $this->memo[$key] = false;
    }

    private function reconstruct($mask, $mod) {
        for ($i = 0; $i < $this->n; $i++) {
            if ((($mask >> $i) & 1) === 0) {
                $nm = ($mod * $this->pows[$i] + $this->nums[$i]) % $this->k;
                if ($this->dp($mask | (1 << $i), $nm)) {
                    $rest = $this->reconstruct($mask | (1 << $i), $nm);
                    array_unshift($rest, $this->nums[$i]);
                    return $rest;
                }
            }
        }
        return [];
    }

    function concatenatedDivisibility($nums, $k) {
        sort($nums);
        $this->nums = array_values($nums);
        $this->k = $k;
        $this->n = count($this->nums);
        $this->pows = array_fill(0, $this->n, 0);
        for ($i = 0; $i < $this->n; $i++) {
            $p = 1;
            $num = $this->nums[$i];
            if ($num === 0) $p = 10 % $k;
            else {
                for ($x = $num; $x > 0; $x = intdiv($x, 10)) $p = $p * 10 % $k;
            }
            $this->pows[$i] = $p;
        }
        $this->memo = [];
        if (!$this->dp(0, 0)) return [];
        return $this->reconstruct(0, 0);
    }
}
