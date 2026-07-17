<?php
// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

class DistanceLimitedPathsExist {
    /** @var int[] */
    private array $weights = [];
    /** @var int[][] */
    private array $versions = [];

    /**
     * @param Integer $n
     * @param Integer[][] $edgeList
     */
    function __construct($n, $edgeList) {
        $edges = [];
        foreach ($edgeList as [$u, $v, $w]) {
            $edges[] = [$w, $u, $v];
        }
        sort($edges);
        $parent = range(0, $n - 1);
        $size = array_fill(0, $n, 1);
        $find = function ($x) use (&$parent) {
            while ($parent[$x] !== $x) {
                $parent[$x] = $parent[$parent[$x]];
                $x = $parent[$x];
            }
            return $x;
        };
        $i = 0;
        $count = count($edges);
        while ($i < $count) {
            $weight = $edges[$i][0];
            while ($i < $count && $edges[$i][0] === $weight) {
                $ra = $find($edges[$i][1]);
                $rb = $find($edges[$i][2]);
                if ($ra !== $rb) {
                    if ($size[$ra] < $size[$rb]) {
                        [$ra, $rb] = [$rb, $ra];
                    }
                    $parent[$rb] = $ra;
                    $size[$ra] += $size[$rb];
                }
                $i++;
            }
            $this->weights[] = $weight;
            $this->versions[] = $parent;
        }
    }

    /**
     * @param Integer $p
     * @param Integer $q
     * @param Integer $limit
     * @return Boolean
     */
    function query($p, $q, $limit) {
        $lo = 0;
        $hi = count($this->weights);
        while ($lo < $hi) {
            $mid = intdiv($lo + $hi, 2);
            if ($this->weights[$mid] < $limit) {
                $lo = $mid + 1;
            } else {
                $hi = $mid;
            }
        }
        $idx = $lo - 1;
        if ($idx < 0) {
            return $p === $q;
        }
        $parent = $this->versions[$idx];
        $rp = $p;
        while ($parent[$rp] !== $rp) {
            $rp = $parent[$rp];
        }
        $rq = $q;
        while ($parent[$rq] !== $rq) {
            $rq = $parent[$rq];
        }
        return $rp === $rq;
    }
}
