<?php
// LeetCode 3508 - Implement Router
// https://leetcode.com/problems/implement-router/

class Router {
    private $lim;
    private $vis;
    private $q;
    private $idx;
    private $d;

    function __construct($memoryLimit) {
        $this->lim = $memoryLimit;
        $this->vis = [];
        $this->q = [];
        $this->idx = [];
        $this->d = [];
    }

    private function f($a, $b, $c) {
        return $a . ',' . $b . ',' . $c;
    }

    function addPacket($source, $destination, $timestamp) {
        $x = $this->f($source, $destination, $timestamp);
        if (isset($this->vis[$x])) return false;
        $this->vis[$x] = true;
        if (count($this->q) >= $this->lim) $this->forwardPacket();
        $this->q[] = [$source, $destination, $timestamp];
        if (!isset($this->d[$destination])) $this->d[$destination] = [];
        $this->d[$destination][] = $timestamp;
        return true;
    }

    function forwardPacket() {
        if (count($this->q) === 0) return [];
        $packet = array_shift($this->q);
        $s = $packet[0];
        $dest = $packet[1];
        $t = $packet[2];
        unset($this->vis[$this->f($s, $dest, $t)]);
        $this->idx[$dest] = ($this->idx[$dest] ?? 0) + 1;
        return [$s, $dest, $t];
    }

    function getCount($destination, $startTime, $endTime) {
        if (!isset($this->d[$destination])) return 0;
        $ls = $this->d[$destination];
        $k = $this->idx[$destination] ?? 0;
        return $this->lowerBound($ls, $k, $endTime + 1) - $this->lowerBound($ls, $k, $startTime);
    }

    private function lowerBound($a, $from, $target) {
        $lo = $from;
        $hi = count($a);
        while ($lo < $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($a[$mid] < $target) $lo = $mid + 1;
            else $hi = $mid;
        }
        return $lo;
    }
}
