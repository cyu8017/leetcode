<?php
// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

class SparseTableRMQ {
    public $n;
    public $fMax;
    public $fMin;
    public $lg;

    function __construct($data) {
        $this->n = count($data);
        $maxLog = 0;
        while ((1 << $maxLog) <= $this->n) $maxLog++;
        $maxLog++;
        $this->fMax = [];
        $this->fMin = [];
        for ($i = 0; $i < $this->n; $i++) {
            $this->fMax[$i] = array_fill(0, $maxLog, 0);
            $this->fMin[$i] = array_fill(0, $maxLog, 0);
        }
        $this->lg = array_fill(0, $this->n + 1, 0);
        for ($i = 2; $i <= $this->n; $i++) $this->lg[$i] = $this->lg[$i >> 1] + 1;
        for ($i = 0; $i < $this->n; $i++) {
            $this->fMax[$i][0] = $data[$i];
            $this->fMin[$i][0] = $data[$i];
        }
        for ($j = 1; $j < $maxLog; $j++) {
            for ($i = 0; $i <= $this->n - (1 << $j); $i++) {
                $this->fMax[$i][$j] = max($this->fMax[$i][$j - 1], $this->fMax[$i + (1 << ($j - 1))][$j - 1]);
                $this->fMin[$i][$j] = min($this->fMin[$i][$j - 1], $this->fMin[$i + (1 << ($j - 1))][$j - 1]);
            }
        }
    }

    function queryMax($l, $r) {
        $k = $this->lg[$r - $l + 1];
        return max($this->fMax[$l][$k], $this->fMax[$r - (1 << $k) + 1][$k]);
    }

    function queryMin($l, $r) {
        $k = $this->lg[$r - $l + 1];
        return min($this->fMin[$l][$k], $this->fMin[$r - (1 << $k) + 1][$k]);
    }
}

class Solution {
    function maxTotalValue($nums, $k) {
        $n = count($nums);
        $st = new SparseTableRMQ($nums);
        $pq = new SplPriorityQueue();
        $pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);
        for ($l = 0; $l < $n; $l++) {
            $val = $st->queryMax($l, $n - 1) - $st->queryMin($l, $n - 1);
            $pq->insert([$val, $l, $n - 1], $val);
        }
        $ans = 0;
        for ($i = 0; $i < $k; $i++) {
            $top = $pq->extract();
            $val = $top[0];
            $l = $top[1];
            $r = $top[2];
            $ans += $val;
            if ($r > $l) {
                $nextVal = $st->queryMax($l, $r - 1) - $st->queryMin($l, $r - 1);
                $pq->insert([$nextVal, $l, $r - 1], $nextVal);
            }
        }
        return $ans;
    }
}
