<?php
// LeetCode 1634 - Add Two Polynomials Represented as Linked Lists
// https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/

class PolyNode {
    public $coefficient;
    public $power;
    public $next;

    function __construct($x = 0, $y = 0, $next = null) {
        $this->coefficient = $x;
        $this->power = $y;
        $this->next = $next;
    }
}

class Solution {
    private function build($items) {
        $dummy = $cur = new PolyNode();
        foreach ($items as $item) {
            $cur->next = new PolyNode($item[0], $item[1]);
            $cur = $cur->next;
        }
        return $dummy->next;
    }

    /**
     * @param PolyNode|Integer[][] $poly1
     * @param PolyNode|Integer[][] $poly2
     * @return PolyNode|Integer[][]
     */
    function addPoly($poly1, $poly2) {
        $listMode = is_array($poly1) || is_array($poly2);
        if (is_array($poly1)) {
            $poly1 = $this->build($poly1);
        }
        if (is_array($poly2)) {
            $poly2 = $this->build($poly2);
        }
        $dummy = $cur = new PolyNode();
        while ($poly1 || $poly2) {
            if (!$poly2 || ($poly1 && $poly1->power > $poly2->power)) {
                $c = $poly1->coefficient;
                $p = $poly1->power;
                $poly1 = $poly1->next;
            } elseif (!$poly1 || $poly2->power > $poly1->power) {
                $c = $poly2->coefficient;
                $p = $poly2->power;
                $poly2 = $poly2->next;
            } else {
                $c = $poly1->coefficient + $poly2->coefficient;
                $p = $poly1->power;
                $poly1 = $poly1->next;
                $poly2 = $poly2->next;
            }
            if ($c) {
                $cur->next = new PolyNode($c, $p);
                $cur = $cur->next;
            }
        }
        if (!$listMode) {
            return $dummy->next;
        }
        $out = [];
        $cur = $dummy->next;
        while ($cur) {
            $out[] = [$cur->coefficient, $cur->power];
            $cur = $cur->next;
        }
        return $out;
    }
}
