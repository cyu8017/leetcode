<?php
// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

$GLOBALS['uniform'] = function () {
    return 0;
};

function set_uniform($uniformFn) {
    $GLOBALS['uniform'] = $uniformFn;
}

class Solution {
    /** @var int[] */
    private array $prefix;

    private int $total;

    /**
     * @param Integer[] $w
     */
    function __construct($w) {
        $this->prefix = [];
        $total = 0;
        foreach ($w as $weight) {
            $total += $weight;
            $this->prefix[] = $total;
        }
        $this->total = $total;
    }

    /**
     * @return Integer
     */
    function pickIndex() {
        $uniform = $GLOBALS['uniform'];
        $target = (int)$uniform(0, $this->total);
        if ($target >= $this->total) {
            $target = $this->total - 1;
        }
        return $this->bisectRight($this->prefix, $target);
    }

    /**
     * @param int[] $arr
     * @param int $target
     * @return int
     */
    private function bisectRight($arr, $target) {
        $low = 0;
        $high = count($arr) - 1;
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if ($arr[$mid] <= $target) {
                $low = $mid + 1;
            } else {
                $high = $mid;
            }
        }
        return $low;
    }
}
