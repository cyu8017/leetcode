<?php
// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

class NumberContainers {
    private $idx;
    private $heap;

    function __construct() {
        $this->idx = [];
        $this->heap = [];
    }

    function change($index, $number) {
        $this->idx[$index] = $number;
        if (!isset($this->heap[$number])) $this->heap[$number] = new SplPriorityQueue();
        $this->heap[$number]->insert($index, -$index);
    }

    function find($number) {
        if (!isset($this->heap[$number])) return -1;
        $h = $this->heap[$number];
        while (!$h->isEmpty()) {
            $i = $h->top();
            if (($this->idx[$i] ?? null) === $number) return $i;
            $h->extract();
        }
        return -1;
    }
}
