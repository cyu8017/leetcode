<?php
// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

class Solution {
    /**
     * @param String $s
     * @param Integer[] $answers
     * @return Integer
     */
    function scoreOfStudents($s, $answers) {
        $evalCorrect = function ($str) {
            $nums = [];
            $ops = [];
            $len = strlen($str);
            for ($i = 0; $i < $len; $i++) {
                $c = $str[$i];
                if ($c >= '0' && $c <= '9') $nums[] = ord($c) - 48;
                else $ops[] = $c;
            }
            $newNums = [$nums[0]];
            $newOps = [];
            $ol = count($ops);
            for ($j = 0; $j < $ol; $j++) {
                if ($ops[$j] === '*') $newNums[count($newNums) - 1] *= $nums[$j + 1];
                else { $newOps[] = $ops[$j]; $newNums[] = $nums[$j + 1]; }
            }
            $res = $newNums[0];
            $nol = count($newOps);
            for ($j = 0; $j < $nol; $j++) $res += $newNums[$j + 1];
            return $res;
        };
        $n = strlen($s);
        $correct = $evalCorrect($s);
        $dp = [];
        for ($i = 0; $i < $n; $i++) $dp[$i] = array_fill(0, $n, null);
        $dfs = null;
        $dfs = function ($l, $r) use (&$dfs, &$dp, $s) {
            if ($dp[$l][$r] !== null) return $dp[$l][$r];
            $res = [];
            if ($l === $r) { $res[ord($s[$l]) - 48] = true; $dp[$l][$r] = $res; return $res; }
            for ($i = $l + 1; $i < $r; $i += 2) {
                foreach ($dfs($l, $i - 1) as $a => $_) {
                    foreach ($dfs($i + 1, $r) as $b => $__) {
                        $v = $s[$i] === '+' ? $a + $b : $a * $b;
                        if ($v <= 1000) $res[$v] = true;
                    }
                }
            }
            $dp[$l][$r] = $res;
            return $res;
        };
        $possible = $dfs(0, $n - 1);
        $ans = 0;
        foreach ($answers as $a) {
            if ($a === $correct) $ans += 5;
            else if (isset($possible[$a])) $ans += 2;
        }
        return $ans;
    }
}
