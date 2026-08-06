<?php

class DSU {
    public $parent;
    public $components;

    function __construct($n) {
        $this->parent = range(0, $n);
        $this->components = $n;
    }

    function find($x) {
        while ($x !== $this->parent[$x]) {
            $this->parent[$x] = $this->parent[$this->parent[$x]];
            $x = $this->parent[$x];
        }
        return $x;
    }

    function union($a, $b) {
        $a = $this->find($a);
        $b = $this->find($b);
        if ($a === $b) {
            return false;
        }
        $this->parent[$a] = $b;
        $this->components--;
        return true;
    }
}

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer
     */
    function maxNumEdgesToRemove($n, $edges) {
        $alice = new DSU($n);
        $bob = new DSU($n);
        $used = 0;

        foreach ($edges as $edge) {
            if ($edge[0] === 3) {
                $merged = $alice->union($edge[1], $edge[2]);
                $bob->union($edge[1], $edge[2]);
                if ($merged) {
                    $used++;
                }
            }
        }

        foreach ($edges as $edge) {
            if ($edge[0] === 1) {
                if ($alice->union($edge[1], $edge[2])) {
                    $used++;
                }
            } elseif ($edge[0] === 2) {
                if ($bob->union($edge[1], $edge[2])) {
                    $used++;
                }
            }
        }

        if ($alice->components === 1 && $bob->components === 1) {
            return count($edges) - $used;
        }
        return -1;
    }
}
