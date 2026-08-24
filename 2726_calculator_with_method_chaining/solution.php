<?php
// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator {
    private $val;

    function __construct($value) {
        $this->val = $value;
    }

    function add($value) {
        $this->val += $value;
        return $this;
    }

    function subtract($value) {
        $this->val -= $value;
        return $this;
    }

    function multiply($value) {
        $this->val *= $value;
        return $this;
    }

    function divide($value) {
        if ($value === 0) throw new Exception("Division by zero is not allowed");
        $this->val /= $value;
        return $this;
    }

    function power($value) {
        $this->val = $this->val ** $value;
        return $this;
    }

    function getResult() {
        return $this->val;
    }
}

class Solution {
    function Calculator($actions = null, $values = null) {
        return new Calculator($values[0] ?? 0);
    }
}
