<?php
// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

class RangeModule {
    private $intervals = [];

    function __construct() {
        $this->intervals = [];
    }

    function addRange($left, $right) {
        $next = [];
        $placed = false;
        foreach ($this->intervals as $iv) {
            $start = $iv[0];
            $end = $iv[1];
            if ($end < $left) $next[] = [$start, $end];
            else if ($right < $start) {
                if (!$placed) { $next[] = [$left, $right]; $placed = true; }
                $next[] = [$start, $end];
            } else {
                $left = min($left, $start);
                $right = max($right, $end);
            }
        }
        if (!$placed) $next[] = [$left, $right];
        $this->intervals = $next;
    }

    function queryRange($left, $right) {
        foreach ($this->intervals as $iv) {
            if ($iv[0] <= $left && $right <= $iv[1]) return true;
            if ($iv[1] >= $right) break;
        }
        return false;
    }

    function removeRange($left, $right) {
        $next = [];
        foreach ($this->intervals as $iv) {
            $start = $iv[0];
            $end = $iv[1];
            if ($end <= $left || $right <= $start) $next[] = [$start, $end];
            else {
                if ($start < $left) $next[] = [$start, $left];
                if ($right < $end) $next[] = [$right, $end];
            }
        }
        $this->intervals = $next;
    }
}
