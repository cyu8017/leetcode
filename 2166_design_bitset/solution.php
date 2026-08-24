<?php
// LeetCode 2166 - Design Bitset
// https://leetcode.com/problems/design-bitset/

class Bitset {
    private $size;
    private $bits;
    private $ones;
    private $flipped;

    /**
     * @param Integer $size
     */
    function __construct($size) {
        $this->size = $size;
        $this->bits = array_fill(0, $size, 0);
        $this->ones = 0;
        $this->flipped = false;
    }

    /**
     * @param Integer $idx
     * @return NULL
     */
    function fix($idx) {
        $target = $this->flipped ? 0 : 1;
        if ($this->bits[$idx] !== $target) {
            $this->bits[$idx] = $target;
            $this->ones += $this->flipped ? -1 : 1;
        }
    }

    /**
     * @param Integer $idx
     * @return NULL
     */
    function unfix($idx) {
        $target = $this->flipped ? 1 : 0;
        if ($this->bits[$idx] !== $target) {
            $this->bits[$idx] = $target;
            $this->ones += $this->flipped ? 1 : -1;
        }
    }

    /**
     * @return NULL
     */
    function flip() {
        $this->flipped = !$this->flipped;
        $this->ones = $this->size - $this->ones;
    }

    /**
     * @return Boolean
     */
    function all() {
        return $this->ones === $this->size;
    }

    /**
     * @return Boolean
     */
    function one() {
        return $this->ones > 0;
    }

    /**
     * @return Integer
     */
    function count() {
        return $this->ones;
    }

    /**
     * @return String
     */
    function toString() {
        $b = [];
        for ($i = 0; $i < $this->size; $i++) {
            $v = $this->bits[$i];
            if ($this->flipped) $v ^= 1;
            $b[] = (string)$v;
        }
        return implode('', $b);
    }
}
