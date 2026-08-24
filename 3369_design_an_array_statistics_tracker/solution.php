<?php
// LeetCode 3369 - Design an Array Statistics Tracker
// https://leetcode.com/problems/design-an-array-statistics-tracker/

class StatisticsTracker {
    public $arr;
    public $sum;
    public $freq;
    public $modeFreq;
    public $modes;

    function __construct() {
        $this->arr = [];
        $this->sum = 0;
        $this->freq = [];
        $this->modeFreq = 0;
        $this->modes = [];
    }

    function addNumber($num) {
        $this->arr[] = $num;
        $this->sum += $num;
        $f = ($this->freq[$num] ?? 0) + 1;
        $this->freq[$num] = $f;
        if ($f > $this->modeFreq) {
            $this->modeFreq = $f;
            $this->modes = [$num => true];
        } else if ($f === $this->modeFreq) {
            $this->modes[$num] = true;
        }
    }

    function removeFirstAddedNumber() {
        if (!$this->arr) return;
        $num = array_shift($this->arr);
        $this->sum -= $num;
        $f = $this->freq[$num] - 1;
        if ($f === 0) unset($this->freq[$num]);
        else $this->freq[$num] = $f;
        $this->modeFreq = 0;
        $this->modes = [];
        foreach ($this->freq as $v => $ff) {
            if ($ff > $this->modeFreq) {
                $this->modeFreq = $ff;
                $this->modes = [$v => true];
            } else if ($ff === $this->modeFreq) {
                $this->modes[$v] = true;
            }
        }
    }

    function getMean() {
        if (!$this->arr) return 0;
        return intdiv($this->sum, count($this->arr));
    }

    function getMedian() {
        $n = count($this->arr);
        $tmp = $this->arr;
        sort($tmp);
        if ($n % 2 === 1) return $tmp[intdiv($n, 2)];
        return $tmp[intdiv($n, 2) - 1];
    }

    function getMode() {
        $best = PHP_INT_MAX;
        foreach ($this->modes as $v => $_) if ($v < $best) $best = $v;
        if ($best === PHP_INT_MAX) return 0;
        return $best;
    }
}
