<?php
// LeetCode 1600 - Throne Inheritance
// https://leetcode.com/problems/throne-inheritance/

class ThroneInheritance {
    private $king;
    private $children = [];
    private $dead = [];

    /**
     * @param String $kingName
     */
    function __construct($kingName) {
        $this->king = $kingName;
    }

    /**
     * @param String $parentName
     * @param String $childName
     * @return NULL
     */
    function birth($parentName, $childName) {
        if (!isset($this->children[$parentName])) {
            $this->children[$parentName] = [];
        }
        $this->children[$parentName][] = $childName;
    }

    /**
     * @param String $name
     * @return NULL
     */
    function death($name) {
        $this->dead[$name] = true;
    }

    /**
     * @return String[]
     */
    function getInheritanceOrder() {
        $order = [];
        $visit = function ($name) use (&$visit, &$order) {
            if (!isset($this->dead[$name])) {
                $order[] = $name;
            }
            foreach ($this->children[$name] ?? [] as $child) {
                $visit($child);
            }
        };
        $visit($this->king);
        return $order;
    }
}
