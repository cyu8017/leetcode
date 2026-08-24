<?php
// LeetCode 3006 - Find Beautiful Indices in the Given Array I
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/

class Solution {
    private function buildLPS(&$lps, $pattern) {
        $l = 0;
        $i = 1;
        $s_l = strlen($pattern);
        $lps[0] = 0;
        while ($i < $s_l) {
            if ($pattern[$i] === $pattern[$l]) {
                $l++;
                $lps[$i] = $l;
                $i++;
            } else if ($l !== 0) {
                $l = $lps[$l - 1];
            } else {
                $lps[$i] = $l;
                $i++;
            }
        }
    }

    private function kmp($s, $pat, $lps, &$index) {
        $s_len = strlen($s);
        $pat_l = strlen($pat);
        $i = 0;
        $j = 0;
        while ($s_len - $i >= $pat_l - $j) {
            if ($s[$i] === $pat[$j]) {
                $i++;
                $j++;
            }
            if ($j === $pat_l) {
                $index[] = $i - $pat_l;
                $j = $lps[$j - 1];
            } else if ($i < $s_len && $s[$i] !== $pat[$j]) {
                if ($j !== 0) $j = $lps[$j - 1];
                else $i++;
            }
        }
    }

    function beautifulIndices($s, $a, $b, $k) {
        $a_len = strlen($a);
        $b_len = strlen($b);
        $lps_a = array_fill(0, $a_len, 0);
        $lps_b = array_fill(0, $b_len, 0);
        $a_index = [];
        $b_index = [];
        $result = [];
        $this->buildLPS($lps_a, $a);
        $this->buildLPS($lps_b, $b);
        $this->kmp($s, $a, $lps_a, $a_index);
        $this->kmp($s, $b, $lps_b, $b_index);
        $i = 0;
        $j = 0;
        while ($i < count($a_index) && $j < count($b_index)) {
            if ($a_index[$i] + $k >= $b_index[$j] && $a_index[$i] - $k <= $b_index[$j]) {
                $result[] = $a_index[$i];
                $i++;
            } else if ($a_index[$i] - $k > $b_index[$j]) {
                $j++;
            } else {
                $i++;
            }
        }
        return $result;
    }
}
