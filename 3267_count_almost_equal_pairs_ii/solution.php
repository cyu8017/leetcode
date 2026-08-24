<?php
// LeetCode 3267 - Count Almost Equal Pairs II
// https://leetcode.com/problems/count-almost-equal-pairs-ii/

class Solution {
    private $sb;

    function countPairs($nums) {
        $ans = 0;
        $n = count($nums);
        for ($i = 0; $i < $n; $i++)
            for ($j = $i + 1; $j < $n; $j++)
                if ($this->almostEqual($nums[$i], $nums[$j])) $ans++;
        return $ans;
    }

    private function dfs(&$arr, $start, $left) {
        if (implode('', $arr) === $this->sb) return true;
        if ($left === 0) return false;
        $len = count($arr);
        for ($i = $start; $i < $len; $i++) {
            if ($arr[$i] === $this->sb[$i]) continue;
            for ($j = $i + 1; $j < $len; $j++) {
                if ($arr[$j] === $this->sb[$i]) {
                    $tmp = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $tmp;
                    if ($this->dfs($arr, $i + 1, $left - 1)) return true;
                    $tmp = $arr[$i]; $arr[$i] = $arr[$j]; $arr[$j] = $tmp;
                }
            }
            return false;
        }
        return implode('', $arr) === $this->sb;
    }

    private function almostEqual($a, $b) {
        $sa = (string)$a;
        $this->sb = (string)$b;
        while (strlen($sa) < strlen($this->sb)) $sa = '0' . $sa;
        while (strlen($this->sb) < strlen($sa)) $this->sb = '0' . $this->sb;
        if ($sa === $this->sb) return true;
        $arr = str_split($sa);
        return $this->dfs($arr, 0, 2);
    }
}
