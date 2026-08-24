<?php
// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

class ZigzagIterator {
    /** @var int[][] */
    private $vectors;
    /** @var int[] */
    private $indices;
    /** @var int */
    private $turn;

    /**
     * @param Integer[] $v1
     * @param Integer[] $v2
     */
    function __construct($v1, $v2) {
        $this->vectors = [$v1, $v2];
        $this->indices = [0, 0];
        $this->turn = 0;
    }

    /**
     * @return Integer
     */
    function next() {
        while ($this->indices[$this->turn] >= count($this->vectors[$this->turn])) {
            $this->turn = 1 - $this->turn;
        }
        $value = $this->vectors[$this->turn][$this->indices[$this->turn]];
        $this->indices[$this->turn] += 1;
        $this->turn = 1 - $this->turn;
        return $value;
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        foreach ($this->indices as $vectorIndex => $index) {
            if ($index < count($this->vectors[$vectorIndex])) {
                return true;
            }
        }
        return false;
    }
}
