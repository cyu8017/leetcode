<?php
// LeetCode 1718 - Construct the Lexicographically Largest Valid Sequence
// https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/

class Solution {
    /**
     * @param Integer $n
     * @return Integer[]
     */
    function constructDistancedSequence($n) {
        $size = 2 * $n - 1;
        $ans = array_fill(0, $size, 0);
        $used = array_fill(0, $n + 1, false);
        $this->backtrack(0, $n, $ans, $used);
        return $ans;
    }

    private function backtrack($i, $n, &$ans, &$used) {
        $size = count($ans);
        while ($i < $size && $ans[$i] !== 0) {
            $i++;
        }
        if ($i === $size) {
            return true;
        }
        for ($value = $n; $value >= 1; $value--) {
            if ($used[$value]) {
                continue;
            }
            if ($value === 1) {
                $ans[$i] = 1;
                $used[1] = true;
                if ($this->backtrack($i + 1, $n, $ans, $used)) {
                    return true;
                }
                $used[1] = false;
                $ans[$i] = 0;
            } else {
                $j = $i + $value;
                if ($j < $size && $ans[$j] === 0) {
                    $ans[$i] = $value;
                    $ans[$j] = $value;
                    $used[$value] = true;
                    if ($this->backtrack($i + 1, $n, $ans, $used)) {
                        return true;
                    }
                    $used[$value] = false;
                    $ans[$i] = 0;
                    $ans[$j] = 0;
                }
            }
        }
        return false;
    }
}
