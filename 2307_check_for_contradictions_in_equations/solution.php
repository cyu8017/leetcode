<?php
// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

class Solution {
    private $parent = [];
    private $weight = [];

    function checkContradictions($equations, $values) {
        $this->parent = [];
        $this->weight = [];
        $n = count($equations);
        for ($i = 0; $i < $n; ++$i) {
            $a = $equations[$i][0];
            $b = $equations[$i][1];
            $ra = $this->find($a);
            $rb = $this->find($b);
            if ($ra === $rb) {
                if (abs($this->weight[$a] / $this->weight[$b] - $values[$i]) > 1e-5) return true;
            } else {
                $this->parent[$ra] = $rb;
                $this->weight[$ra] = $values[$i] * $this->weight[$b] / $this->weight[$a];
            }
        }
        return false;
    }

    private function find($x) {
        if (!isset($this->parent[$x])) {
            $this->parent[$x] = $x;
            $this->weight[$x] = 1.0;
            return $x;
        }
        if ($this->parent[$x] !== $x) {
            $p = $this->find($this->parent[$x]);
            $this->weight[$x] = $this->weight[$x] * $this->weight[$this->parent[$x]];
            $this->parent[$x] = $p;
        }
        return $this->parent[$x];
    }
}
