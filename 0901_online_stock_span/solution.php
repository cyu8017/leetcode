<?php
// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

class StockSpanner {
    private $stack;

    function __construct() {
        $this->stack = [];
    }

    function next($price) {
        $span = 1;
        while ($this->stack && $this->stack[count($this->stack) - 1][0] <= $price) {
            $span += $this->stack[count($this->stack) - 1][1];
            array_pop($this->stack);
        }
        $this->stack[] = [$price, $span];
        return $span;
    }
}
