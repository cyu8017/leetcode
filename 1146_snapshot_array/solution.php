<?php
// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

class SnapshotArray {
    private $snapId = 0;
    private $data = [];

    /**
     * @param Integer $length
     */
    function __construct($length) {
        for ($i = 0; $i < $length; $i++) {
            $this->data[$i] = [[0, 0]];
        }
    }

    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function set($index, $val) {
        $hist = &$this->data[$index];
        $last = count($hist) - 1;
        if ($hist[$last][0] === $this->snapId) {
            $hist[$last][1] = $val;
        } else {
            $hist[] = [$this->snapId, $val];
        }
    }

    /**
     * @return Integer
     */
    function snap() {
        return $this->snapId++;
    }

    /**
     * @param Integer $index
     * @param Integer $snap_id
     * @return Integer
     */
    function get($index, $snap_id) {
        $hist = $this->data[$index];
        $lo = 0;
        $hi = count($hist) - 1;
        $ans = 0;
        while ($lo <= $hi) {
            $mid = ($lo + $hi) >> 1;
            if ($hist[$mid][0] <= $snap_id) {
                $ans = $mid;
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return $hist[$ans][1];
    }
}
