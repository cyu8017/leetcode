<?php
// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

class Solution {
    private function lcpOf($a) {
        if (!count($a)) return 0;
        $pref = $a[0];
        for ($t = 1; $t < count($a); $t++) {
            $s = $a[$t];
            $i = 0;
            $pn = strlen($pref);
            $sn = strlen($s);
            while ($i < $pn && $i < $sn && $pref[$i] === $s[$i]) $i++;
            $pref = substr($pref, 0, $i);
            if (!strlen($pref)) return 0;
        }
        return strlen($pref);
    }

    function longestCommonPrefix($words, $k) {
        $n = count($words);
        $ans = array_fill(0, $n, 0);
        for ($i = 0; $i < $n; $i++) {
            $rest = [];
            for ($j = 0; $j < $n; $j++) if ($j !== $i) $rest[] = $words[$j];
            if (count($rest) < $k) { $ans[$i] = 0; continue; }
            sort($rest);
            $best = 0;
            for ($j = 0; $j + $k - 1 < count($rest); $j++) {
                $best = max($best, $this->lcpOf(array_slice($rest, $j, $k)));
            }
            $ans[$i] = $best;
        }
        return $ans;
    }
}
