<?php
// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

class MaxStack {
    private $stack = [];
    private $maxes = [];

    function __construct() {
        $this->stack = [];
        $this->maxes = [];
    }

    function push($x) {
        $this->stack[] = $x;
        $this->maxes[] = count($this->maxes) === 0 ? $x : max($x, $this->maxes[count($this->maxes) - 1]);
    }

    function pop() {
        array_pop($this->maxes);
        return array_pop($this->stack);
    }

    function top() { return $this->stack[count($this->stack) - 1]; }

    function peekMax() { return $this->maxes[count($this->maxes) - 1]; }

    function popMax() {
        $maxVal = $this->peekMax();
        $buffer = [];
        while ($this->top() !== $maxVal) $buffer[] = $this->pop();
        $this->pop();
        for ($i = count($buffer) - 1; $i >= 0; $i--) $this->push($buffer[$i]);
        return $maxVal;
    }
}
