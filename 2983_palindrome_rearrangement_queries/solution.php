<?php
// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

class Solution {
    private function countPref($pre, $i, $j) {
        $cnt = [];
        for ($k = 0; $k < 26; $k++) $cnt[$k] = $pre[$j + 1][$k] - $pre[$i][$k];
        return $cnt;
    }

    private function subCnt($cnt1, $cnt2) {
        $cnt = [];
        for ($i = 0; $i < 26; $i++) {
            $cnt[$i] = $cnt1[$i] - $cnt2[$i];
            if ($cnt[$i] < 0) return null;
        }
        return $cnt;
    }

    private function eqCnt($a, $b) {
        for ($i = 0; $i < 26; $i++) if ($a[$i] !== $b[$i]) return false;
        return true;
    }

    private function check($pre1, $pre2, $diff, $a, $b, $c, $d) {
        if ($diff[$a] > 0 || $diff[count($diff) - 1] - $diff[max($b, $d) + 1] > 0) return false;
        if ($d <= $b) return $this->eqCnt($this->countPref($pre1, $a, $b), $this->countPref($pre2, $a, $b));
        if ($b < $c) {
            return $diff[$c] - $diff[$b + 1] === 0
                && $this->eqCnt($this->countPref($pre1, $a, $b), $this->countPref($pre2, $a, $b))
                && $this->eqCnt($this->countPref($pre1, $c, $d), $this->countPref($pre2, $c, $d));
        }
        $cnt1 = $this->subCnt($this->countPref($pre1, $a, $b), $this->countPref($pre2, $a, $c - 1));
        $cnt2 = $this->subCnt($this->countPref($pre2, $c, $d), $this->countPref($pre1, $b + 1, $d));
        return $cnt1 !== null && $cnt2 !== null && $this->eqCnt($cnt1, $cnt2);
    }

    function canMakePalindromeQueries($s, $queries) {
        $n = strlen($s);
        $m = intdiv($n, 2);
        $t = strrev(substr($s, $m));
        $s = substr($s, 0, $m);
        $pre1 = [];
        $pre2 = [];
        $pre1[0] = array_fill(0, 26, 0);
        $pre2[0] = array_fill(0, 26, 0);
        $diff = array_fill(0, $m + 1, 0);
        for ($i = 1; $i <= $m; $i++) {
            $pre1[$i] = $pre1[$i - 1];
            $pre2[$i] = $pre2[$i - 1];
            $pre1[$i][ord($s[$i - 1]) - 97]++;
            $pre2[$i][ord($t[$i - 1]) - 97]++;
            $diff[$i] = $diff[$i - 1] + ($s[$i - 1] === $t[$i - 1] ? 0 : 1);
        }
        $ans = [];
        for ($i = 0; $i < count($queries); $i++) {
            $q = $queries[$i];
            $a = $q[0];
            $b = $q[1];
            $c = $n - 1 - $q[3];
            $d = $n - 1 - $q[2];
            $ans[] = ($a <= $c)
                ? $this->check($pre1, $pre2, $diff, $a, $b, $c, $d)
                : $this->check($pre2, $pre1, $diff, $c, $d, $a, $b);
        }
        return $ans;
    }
}
