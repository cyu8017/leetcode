<?php
// LeetCode 2157 - Groups of Strings
// https://leetcode.com/problems/groups-of-strings/

class Solution {
    private $parent = [];
    private $size = [];

    private function find($x) {
        if ($this->parent[$x] !== $x) $this->parent[$x] = $this->find($this->parent[$x]);
        return $this->parent[$x];
    }

    private function unite($a, $b) {
        $ra = $this->find($a);
        $rb = $this->find($b);
        if ($ra === $rb) return;
        if ($this->size[$ra] < $this->size[$rb]) {
            $t = $ra;
            $ra = $rb;
            $rb = $t;
        }
        $this->parent[$rb] = $ra;
        $this->size[$ra] += $this->size[$rb];
    }

    /**
     * @param String[] $words
     * @return Integer[]
     */
    function groupStrings($words) {
        $freq = [];
        foreach ($words as $w) {
            $m = 0;
            $len = strlen($w);
            for ($i = 0; $i < $len; $i++) $m |= 1 << (ord($w[$i]) - 97);
            $freq[$m] = ($freq[$m] ?? 0) + 1;
        }
        $this->parent = [];
        $this->size = [];
        foreach ($freq as $k => $v) {
            $this->parent[$k] = $k;
            $this->size[$k] = $v;
        }
        foreach ($freq as $m => $_) {
            for ($b = 0; $b < 26; $b++) {
                if (($m & (1 << $b)) !== 0) {
                    $nm = $m ^ (1 << $b);
                    if (isset($freq[$nm])) $this->unite($m, $nm);
                    for ($a = 0; $a < 26; $a++) {
                        if (($nm & (1 << $a)) === 0) {
                            $rm = $nm | (1 << $a);
                            if (isset($freq[$rm])) $this->unite($m, $rm);
                        }
                    }
                } else {
                    $nm = $m | (1 << $b);
                    if (isset($freq[$nm])) $this->unite($m, $nm);
                }
            }
        }
        $groups = 0;
        $maxSize = 0;
        $seen = [];
        foreach ($freq as $m => $_) {
            $r = $this->find($m);
            if (!isset($seen[$r])) {
                $seen[$r] = true;
                $groups++;
                $maxSize = max($maxSize, $this->size[$r]);
            }
        }
        return [$groups, $maxSize];
    }
}
