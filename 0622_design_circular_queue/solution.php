<?php
// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue {
    private $data;
    private $capacity;
    private $head = 0;
    private $size = 0;

    function __construct($k) {
        $this->data = array_fill(0, $k, 0);
        $this->capacity = $k;
    }

    function enQueue($value) {
        if ($this->isFull()) return false;
        $this->data[($this->head + $this->size) % $this->capacity] = $value;
        ++$this->size;
        return true;
    }

    function deQueue() {
        if ($this->isEmpty()) return false;
        $this->head = ($this->head + 1) % $this->capacity;
        --$this->size;
        return true;
    }

    function Front() {
        return $this->isEmpty() ? -1 : $this->data[$this->head];
    }

    function Rear() {
        if ($this->isEmpty()) return -1;
        return $this->data[($this->head + $this->size - 1) % $this->capacity];
    }

    function isEmpty() {
        return $this->size === 0;
    }

    function isFull() {
        return $this->size === $this->capacity;
    }
}
