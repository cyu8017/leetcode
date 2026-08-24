<?php
// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

class Solution {
    private $parent;

    private function find($x) {
        if ($this->parent[$x] === $x) return $x;
        return $this->parent[$x] = $this->find($this->parent[$x]);
    }

    private function unite($a, $b) {
        $a = $this->find($a);
        $b = $this->find($b);
        if ($a !== $b) $this->parent[$a] = $b;
    }

    /**
     * @param Integer $n
     * @param Integer[][] $meetings
     * @param Integer $firstPerson
     * @return Integer[]
     */
    function findAllPeople($n, $meetings, $firstPerson) {
        usort($meetings, function($a, $b) { return $a[2] - $b[2]; });
        $this->parent = range(0, $n - 1);
        $know = array_fill(0, $n, false);
        $know[0] = true;
        $know[$firstPerson] = true;
        $this->unite(0, $firstPerson);
        $m = count($meetings);
        $i = 0;
        while ($i < $m) {
            $j = $i;
            while ($j < $m && $meetings[$j][2] === $meetings[$i][2]) $j++;
            for ($k = $i; $k < $j; $k++) $this->unite($meetings[$k][0], $meetings[$k][1]);
            $root0 = $this->find(0);
            $reset = [];
            for ($k = $i; $k < $j; $k++) {
                $a = $meetings[$k][0];
                $b = $meetings[$k][1];
                if ($this->find($a) !== $root0) {
                    $reset[] = $a;
                    $reset[] = $b;
                } else {
                    $know[$a] = true;
                    $know[$b] = true;
                }
            }
            foreach ($reset as $x) $this->parent[$x] = $x;
            $i = $j;
        }
        $ans = [];
        $f0 = $this->find(0);
        for ($i = 0; $i < $n; $i++) {
            if ($this->find($i) === $f0 || $know[$i]) $ans[] = $i;
        }
        return $ans;
    }
}
