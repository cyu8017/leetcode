<?php
// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

class DinnerPlates {
    private $capacity;
    private $stacks = [];
    private $available;

    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        $this->capacity = $capacity;
        $this->available = new SplMinHeap();
    }

    /**
     * @param Integer $val
     * @return NULL
     */
    function push($val) {
        while (!$this->available->isEmpty()) {
            $top = $this->available->top();
            if ($top >= count($this->stacks) || count($this->stacks[$top]) === $this->capacity) {
                $this->available->extract();
            } else break;
        }
        if ($this->available->isEmpty()) {
            $this->stacks[] = [];
            $this->available->insert(count($this->stacks) - 1);
        }
        $idx = $this->available->top();
        $this->stacks[$idx][] = $val;
        if (count($this->stacks[$idx]) === $this->capacity) {
            $this->available->extract();
        }
    }

    /**
     * @return Integer
     */
    function pop() {
        while (!empty($this->stacks) && empty($this->stacks[count($this->stacks) - 1])) {
            array_pop($this->stacks);
        }
        return empty($this->stacks) ? -1 : $this->popAtStack(count($this->stacks) - 1);
    }

    /**
     * @param Integer $index
     * @return Integer
     */
    function popAtStack($index) {
        if ($index < 0 || $index >= count($this->stacks) || empty($this->stacks[$index])) return -1;
        if (count($this->stacks[$index]) === $this->capacity) {
            $this->available->insert($index);
        }
        return array_pop($this->stacks[$index]);
    }
}
