<?php
// LeetCode 1286 - Iterator for Combination
// https://leetcode.com/problems/iterator-for-combination/

class CombinationIterator {
    private $items = [];
    private $index = 0;

    /**
     * @param String $characters
     * @param Integer $combinationLength
     */
    function __construct($characters, $combinationLength) {
        $chars = str_split($characters);
        $n = count($chars);
        $dfs = function ($start, $path) use (&$dfs, $chars, $n, $combinationLength) {
            if (count($path) === $combinationLength) {
                $this->items[] = implode('', $path);
                return;
            }
            for ($i = $start; $i < $n; $i++) {
                $path[] = $chars[$i];
                $dfs($i + 1, $path);
                array_pop($path);
            }
        };
        $dfs(0, []);
    }

    /**
     * @return String
     */
    function next() {
        return $this->items[$this->index++];
    }

    /**
     * @return Boolean
     */
    function hasNext() {
        return $this->index < count($this->items);
    }
}
