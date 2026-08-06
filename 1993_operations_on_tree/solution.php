<?php
// LeetCode 1993 - Operations on Tree
// https://leetcode.com/problems/operations-on-tree/

class LockingTree {
    private $locked;
    private $parent;
    private $children;

    /**
     * @param Integer[] $parent
     */
    function __construct($parent) {
        $n = count($parent);
        $this->locked = array_fill(0, $n, -1);
        $this->parent = $parent;
        $this->children = array_fill(0, $n, []);
        for ($son = 1; $son < $n; $son++) {
            $this->children[$parent[$son]][] = $son;
        }
    }

    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function lock($num, $user) {
        if ($this->locked[$num] === -1) {
            $this->locked[$num] = $user;
            return true;
        }
        return false;
    }

    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function unlock($num, $user) {
        if ($this->locked[$num] === $user) {
            $this->locked[$num] = -1;
            return true;
        }
        return false;
    }

    /**
     * @param Integer $num
     * @param Integer $user
     * @return Boolean
     */
    function upgrade($num, $user) {
        $x = $num;
        while ($x !== -1) {
            if ($this->locked[$x] !== -1) {
                return false;
            }
            $x = $this->parent[$x];
        }

        $find = false;
        $this->dfsUnlock($num, $find);
        if (!$find) {
            return false;
        }
        $this->locked[$num] = $user;
        return true;
    }

    private function dfsUnlock($u, &$find) {
        foreach ($this->children[$u] as $v) {
            if ($this->locked[$v] !== -1) {
                $this->locked[$v] = -1;
                $find = true;
            }
            $this->dfsUnlock($v, $find);
        }
    }
}
