<?php
// LeetCode 1722 - Minimize Hamming Distance After Swap Operations
// https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/

class Solution {
    private $parent;

    /**
     * @param Integer[] $source
     * @param Integer[] $target
     * @param Integer[][] $allowedSwaps
     * @return Integer
     */
    function minimumHammingDistance($source, $target, $allowedSwaps) {
        $n = count($source);
        $this->parent = range(0, $n - 1);
        foreach ($allowedSwaps as [$a, $b]) {
            $this->union($a, $b);
        }
        $groups = [];
        for ($i = 0; $i < $n; $i++) {
            $root = $this->find($i);
            if (!isset($groups[$root][$source[$i]])) {
                $groups[$root][$source[$i]] = 0;
            }
            $groups[$root][$source[$i]]++;
        }
        $ans = 0;
        for ($i = 0; $i < $n; $i++) {
            $root = $this->find($i);
            if (!empty($groups[$root][$target[$i]])) {
                $groups[$root][$target[$i]]--;
            } else {
                $ans++;
            }
        }
        return $ans;
    }

    private function find($x) {
        while ($this->parent[$x] !== $x) {
            $this->parent[$x] = $this->parent[$this->parent[$x]];
            $x = $this->parent[$x];
        }
        return $x;
    }

    private function union($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra !== $rb) {
            $this->parent[$rb] = $ra;
        }
    }
}
