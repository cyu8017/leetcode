<?php
// LeetCode 1505 - Minimum Possible Integer After at Most K Adjacent Swaps On Digits
// https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/

class Fenwick {
    private $bit;

    function __construct($n) {
        $this->bit = array_fill(0, $n + 1, 0);
    }

    function add($i, $delta) {
        $i += 1;
        $len = count($this->bit);
        while ($i < $len) {
            $this->bit[$i] += $delta;
            $i += $i & -$i;
        }
    }

    function sum($i) {
        $out = 0;
        while ($i > 0) {
            $out += $this->bit[$i];
            $i -= $i & -$i;
        }
        return $out;
    }
}

class Solution {
    /**
     * @param String $num
     * @param Integer $k
     * @return String
     */
    function minInteger($num, $k) {
        $positions = array_fill(0, 10, []);
        $n = strlen($num);
        for ($i = 0; $i < $n; $i++) {
            $positions[(int)$num[$i]][] = $i;
        }
        $heads = array_fill(0, 10, 0);
        $fw = new Fenwick($n);
        $out = '';
        for ($t = 0; $t < $n; $t++) {
            for ($digit = 0; $digit < 10; $digit++) {
                if ($heads[$digit] >= count($positions[$digit])) {
                    continue;
                }
                $index = $positions[$digit][$heads[$digit]];
                $cost = $index - $fw->sum($index);
                if ($cost <= $k) {
                    $k -= $cost;
                    $heads[$digit]++;
                    $fw->add($index, 1);
                    $out .= (string)$digit;
                    break;
                }
            }
        }
        return $out;
    }
}
