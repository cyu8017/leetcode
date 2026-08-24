<?php
// LeetCode 0380 - Insert Delete GetRandom O(1)
// https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet {
    /** @var int[] */
    private array $values = [];

    /** @var array<int, int> */
    private array $index_by_value = [];

    /**
     * @param Integer $val
     * @return Boolean
     */
    function insert($val) {
        if (isset($this->index_by_value[$val])) {
            return false;
        }

        $this->index_by_value[$val] = count($this->values);
        $this->values[] = $val;
        return true;
    }

    /**
     * @param Integer $val
     * @return Boolean
     */
    function remove($val) {
        if (!isset($this->index_by_value[$val])) {
            return false;
        }

        $index = $this->index_by_value[$val];
        $lastValue = $this->values[count($this->values) - 1];
        $this->values[$index] = $lastValue;
        $this->index_by_value[$lastValue] = $index;
        array_pop($this->values);
        unset($this->index_by_value[$val]);
        return true;
    }

    /**
     * @return Integer
     */
    function getRandom() {
        return $this->get_random();
    }

    /**
     * @return Integer
     */
    function get_random() {
        return $this->values[array_rand($this->values)];
    }
}
