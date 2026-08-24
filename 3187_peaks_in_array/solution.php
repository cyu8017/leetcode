<?php
// LeetCode 3187 - Peaks in Array
// https://leetcode.com/problems/peaks-in-array/

class Solution {
    private $bitN;
    private $bitC;
    private $nums;
    private $n;

    function countOfPeaks($nums, $queries) {
        $this->nums = $nums;
        $this->n = count($nums);
        $this->bitN = $this->n - 1;
        $this->bitC = array_fill(0, $this->bitN + 1, 0);
        for ($i = 1; $i < $this->n - 1; $i++) $this->updatePeak($i, 1);
        $ans = [];
        foreach ($queries as $q) {
            if ($q[0] === 1) {
                $l = $q[1] + 1;
                $r = $q[2] - 1;
                $t = 0;
                if ($l <= $r) $t = $this->bitQuery($r) - $this->bitQuery($l - 1);
                $ans[] = $t;
            } else {
                $idx = $q[1];
                $val = $q[2];
                for ($i = $idx - 1; $i <= $idx + 1; $i++) $this->updatePeak($i, -1);
                $this->nums[$idx] = $val;
                for ($i = $idx - 1; $i <= $idx + 1; $i++) $this->updatePeak($i, 1);
            }
        }
        return $ans;
    }

    private function bitUpdate($x, $delta) {
        for (; $x <= $this->bitN; $x += $x & -$x) $this->bitC[$x] += $delta;
    }

    private function bitQuery($x) {
        $s = 0;
        for (; $x > 0; $x -= $x & -$x) $s += $this->bitC[$x];
        return $s;
    }

    private function updatePeak($i, $val) {
        if ($i <= 0 || $i >= $this->n - 1) return;
        if ($this->nums[$i - 1] < $this->nums[$i] && $this->nums[$i] > $this->nums[$i + 1]) $this->bitUpdate($i, $val);
    }
}
