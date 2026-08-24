<?php
// LeetCode 0385 - Mini Parser
// https://leetcode.com/problems/mini-parser/

class NestedInteger {
    private $integer = null;
    private $list = [];

    function __construct($value = null) {
        if (is_int($value)) {
            $this->integer = $value;
        }
    }

    function isInteger() {
        return $this->integer !== null;
    }

    function getInteger() {
        return $this->integer ?? 0;
    }

    function getList() {
        return $this->list;
    }

    function add($item) {
        $this->list[] = $item;
    }
}

class Solution {
    /**
     * @param String $s
     * @return NestedInteger
     */
    function deserialize($s) {
        if ($s[0] !== '[') {
            return new NestedInteger((int)$s);
        }

        $stack = [];
        $current = null;
        $index = 0;
        $negative = false;
        $number = 0;
        $hasNumber = false;
        $length = strlen($s);

        while ($index < $length) {
            $char = $s[$index];
            if ($char === '[') {
                $item = new NestedInteger();
                if ($current !== null) {
                    $stack[] = $current;
                }
                $current = $item;
            } elseif ($char === '-') {
                $negative = true;
            } elseif ($char >= '0' && $char <= '9') {
                $number = $number * 10 + (int)$char;
                $hasNumber = true;
            } elseif ($char === ',' || $char === ']') {
                if ($hasNumber) {
                    $value = $negative ? -$number : $number;
                    $current->add(new NestedInteger($value));
                    $number = 0;
                    $negative = false;
                    $hasNumber = false;
                }
                if ($char === ']') {
                    if (count($stack) === 0) {
                        return $current;
                    }
                    $parent = array_pop($stack);
                    $parent->add($current);
                    $current = $parent;
                }
            }
            $index++;
        }

        return $current ?? new NestedInteger();
    }
}
