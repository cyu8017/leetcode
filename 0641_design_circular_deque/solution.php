<?php
// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

class MyCircularDeque {
    private $data;
    private $capacity;
    private $front = 0;
    private $size = 0;

    function __construct($k) {
        $this->data = array_fill(0, $k, 0);
        $this->capacity = $k;
    }

    function insertFront($value) {
        if ($this->isFull()) return false;
        $this->front = ($this->front - 1 + $this->capacity) % $this->capacity;
        $this->data[$this->front] = $value;
        ++$this->size;
        return true;
    }

    function insertLast($value) {
        if ($this->isFull()) return false;
        $this->data[($this->front + $this->size) % $this->capacity] = $value;
        ++$this->size;
        return true;
    }

    function deleteFront() {
        if ($this->isEmpty()) return false;
        $this->front = ($this->front + 1) % $this->capacity;
        --$this->size;
        return true;
    }

    function deleteLast() {
        if ($this->isEmpty()) return false;
        --$this->size;
        return true;
    }

    function getFront() {
        return $this->isEmpty() ? -1 : $this->data[$this->front];
    }

    function getRear() {
        if ($this->isEmpty()) return -1;
        return $this->data[($this->front + $this->size - 1) % $this->capacity];
    }

    function isEmpty() {
        return $this->size === 0;
    }

    function isFull() {
        return $this->size === $this->capacity;
    }
}
