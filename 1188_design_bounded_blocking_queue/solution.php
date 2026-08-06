<?php
// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

class BoundedBlockingQueue {
    private $capacity;
    private $queue = [];

    /**
     * @param Integer $capacity
     */
    function __construct($capacity) {
        $this->capacity = $capacity;
    }

    /**
     * @param Integer $element
     * @return NULL
     */
    function enqueue($element) {
        while (count($this->queue) >= $this->capacity) { usleep(100); }
        $this->queue[] = $element;
    }

    /**
     * @return Integer
     */
    function dequeue() {
        while (empty($this->queue)) { usleep(100); }
        return array_shift($this->queue);
    }

    /**
     * @return Integer
     */
    function size() {
        return count($this->queue);
    }
}
