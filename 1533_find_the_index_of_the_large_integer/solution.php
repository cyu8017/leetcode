<?php

class ArrayReader {
    /** @var int[] */
    private $arr;

    /**
     * @param int[] $arr
     */
    function __construct($arr) {
        $this->arr = $arr;
    }

    /**
     * @param Integer $l
     * @param Integer $r
     * @param Integer $x
     * @param Integer $y
     * @return Integer
     */
    function compareSub($l, $r, $x, $y) {
        $a = 0;
        for ($i = $l; $i <= $r; $i++) {
            $a += $this->arr[$i];
        }
        $b = 0;
        for ($i = $x; $i <= $y; $i++) {
            $b += $this->arr[$i];
        }
        if ($a > $b) {
            return 1;
        }
        if ($a < $b) {
            return -1;
        }
        return 0;
    }

    /**
     * @return Integer
     */
    function length() {
        return count($this->arr);
    }
}

class Solution {
    /**
     * @param ArrayReader|Integer[] $reader
     * @return Integer
     */
    function getIndex($reader) {
        if (is_array($reader)) {
            $reader = new ArrayReader($reader);
        }
        $left = 0;
        $right = $reader->length() - 1;
        while ($left < $right) {
            $length = $right - $left + 1;
            $half = intdiv($length, 2);
            $result = $reader->compareSub($left, $left + $half - 1, $right - $half + 1, $right);
            if ($result === 0) {
                return $left + $half;
            }
            if ($result > 0) {
                $right = $left + $half - 1;
            } else {
                $left = $right - $half + 1;
            }
        }
        return $left;
    }
}
