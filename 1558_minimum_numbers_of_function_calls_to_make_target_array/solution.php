<?php

class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function minOperations($nums) {
        $adds = 0;
        $maxDoubles = 0;
        foreach ($nums as $x) {
            $adds += $this->bitCount($x);
            $len = $this->bitLength($x);
            if ($len > 0) {
                $maxDoubles = max($maxDoubles, $len - 1);
            }
        }
        return $adds + $maxDoubles;
    }

    private function bitCount($x) {
        $count = 0;
        while ($x > 0) {
            $count += $x & 1;
            $x >>= 1;
        }
        return $count;
    }

    private function bitLength($x) {
        $len = 0;
        while ($x > 0) {
            $len++;
            $x >>= 1;
        }
        return $len;
    }
}
