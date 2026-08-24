<?php
// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

class TimeMap {
    private $times = [];
    private $vals = [];

    function __construct() {
        $this->times = [];
        $this->vals = [];
    }

    /**
     * @param String $key
     * @param String $value
     * @param Integer $timestamp
     * @return NULL
     */
    function set($key, $value, $timestamp) {
        if (!isset($this->times[$key])) {
            $this->times[$key] = [];
            $this->vals[$key] = [];
        }
        $this->times[$key][] = $timestamp;
        $this->vals[$key][] = $value;
    }

    /**
     * @param String $key
     * @param Integer $timestamp
     * @return String
     */
    function get($key, $timestamp) {
        if (!isset($this->times[$key])) return "";
        $tarr = $this->times[$key];
        $varr = $this->vals[$key];
        $lo = 0;
        $hi = count($tarr) - 1;
        $ans = -1;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($tarr[$mid] <= $timestamp) { $ans = $mid; $lo = $mid + 1; }
            else $hi = $mid - 1;
        }
        return $ans < 0 ? "" : $varr[$ans];
    }
}
