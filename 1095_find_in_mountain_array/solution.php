<?php
// LeetCode 1095 - Find in Mountain Array
// https://leetcode.com/problems/find-in-mountain-array/

class MountainArray {
    /**
     * @param Integer $index
     * @return Integer
     */
    function get($index) {
        throw new Exception("Not implemented");
    }

    /**
     * @return Integer
     */
    function length() {
        throw new Exception("Not implemented");
    }
}

class Solution {
    /**
     * @param Integer $target
     * @param MountainArray $mountainArr
     * @return Integer
     */
    function findInMountainArray($target, $mountainArr) {
        $n = $mountainArr->length();
        $lo = 0;
        $hi = $n - 1;
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($mountainArr->get($mid) < $mountainArr->get($mid + 1)) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        $peak = $lo;
        $lo = 0;
        $hi = $peak;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $val = $mountainArr->get($mid);
            if ($val === $target) {
                return $mid;
            }
            if ($val < $target) {
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        $lo = $peak + 1;
        $hi = $n - 1;
        while ($lo <= $hi) {
            $mid = intdiv($lo + $hi, 2);
            $val = $mountainArr->get($mid);
            if ($val === $target) {
                return $mid;
            }
            if ($val > $target) {
                $lo = $mid + 1;
            } else {
                $hi = $mid - 1;
            }
        }
        return -1;
    }
}
