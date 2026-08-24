<?php
// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

class Solution {
    public $parent;

    function gcd($a, $b) {
        while ($b !== 0) { $t = $a % $b; $a = $b; $b = $t; }
        return $a;
    }

    function find($x) {
        if ($this->parent[$x] !== $x) $this->parent[$x] = $this->find($this->parent[$x]);
        return $this->parent[$x];
    }

    function unite($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra !== $rb) $this->parent[$ra] = $rb;
    }

    function countComponents($nums, $threshold) {
        $n = count($nums);
        $this->parent = range(0, $n - 1);
        $idx = [];
        for ($i = 0; $i < $n; $i++) $idx[$nums[$i]] = $i;
        for ($d = 1; $d <= $threshold; $d++) {
            $first = -1;
            for ($m = $d; $m <= $threshold; $m += $d) {
                if (isset($idx[$m])) {
                    $i = $idx[$m];
                    if ($first === -1) $first = $i;
                    else if (intdiv($nums[$first] * $nums[$i], $this->gcd($nums[$first], $nums[$i])) <= $threshold)
                        $this->unite($first, $i);
                }
            }
        }
        for ($i = 0; $i < $n; $i++) {
            for ($j = $i + 1; $j < $n; $j++) {
                $a = $nums[$i];
                $b = $nums[$j];
                $g = $this->gcd($a, $b);
                if (intdiv($a, $g) * $b <= $threshold) $this->unite($i, $j);
            }
        }
        $comp = [];
        for ($i = 0; $i < $n; $i++) $comp[$this->find($i)] = true;
        return count($comp);
    }
}
