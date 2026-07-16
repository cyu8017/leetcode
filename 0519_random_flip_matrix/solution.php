<?php
// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

$uniform = null;

function set_uniform($fn) {
    global $uniform;
    $uniform = $fn;
}

class Solution {
    /** @var int */
    private $cols;

    /** @var int */
    private $total;

    /** @var int[] */
    private $available;

    /**
     * @param int $m
     * @param int $n
     */
    function __construct($m, $n) {
        $this->cols = $n;
        $this->total = $m * $n;
        $this->reset();
    }

    /**
     * @return int[]
     */
    function flip() {
        global $uniform;
        $index = (int) $uniform(0, count($this->available) - 1);
        if ($index >= count($this->available)) {
            $index = count($this->available) - 1;
        }
        $value = $this->available[$index];
        $this->available[$index] = $this->available[count($this->available) - 1];
        array_pop($this->available);
        return [intdiv($value, $this->cols), $value % $this->cols];
    }

    function reset() {
        $this->available = range(0, $this->total - 1);
    }
}
