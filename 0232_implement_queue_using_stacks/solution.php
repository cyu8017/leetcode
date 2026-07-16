<?php

// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue {
    private $inputStack = [];
    private $outputStack = [];

    private function move() {
        if (count($this->outputStack) === 0) {
            while (count($this->inputStack) > 0) {
                $this->outputStack[] = array_pop($this->inputStack);
            }
        }
    }

    function push($x) {
        $this->inputStack[] = $x;
    }

    function pop() {
        $this->move();
        return array_pop($this->outputStack);
    }

    function peek() {
        $this->move();
        return $this->outputStack[count($this->outputStack) - 1];
    }

    function empty() {
        return count($this->inputStack) === 0 && count($this->outputStack) === 0;
    }
}
