<?php
// LeetCode 1998 - GCD Sort of an Array
// https://leetcode.com/problems/gcd-sort-of-an-array/

class Solution {
    private $parent;

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function gcdSort($nums) {
        $m = max($nums);
        $this->parent = range(0, $m);

        $spf = range(0, $m);
        $limit = (int)sqrt($m);
        for ($i = 2; $i <= $limit; $i++) {
            if ($spf[$i] === $i) {
                for ($j = $i * $i; $j <= $m; $j += $i) {
                    if ($spf[$j] === $j) {
                        $spf[$j] = $i;
                    }
                }
            }
        }

        $unique = array_unique($nums);
        foreach ($unique as $x) {
            $y = $x;
            while ($y > 1) {
                $p = $spf[$y];
                $this->union($x, $p);
                while ($y % $p === 0) {
                    $y = intdiv($y, $p);
                }
            }
        }

        $sorted = $nums;
        sort($sorted);
        $n = count($nums);
        for ($i = 0; $i < $n; $i++) {
            if ($this->find($nums[$i]) !== $this->find($sorted[$i])) {
                return false;
            }
        }
        return true;
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
