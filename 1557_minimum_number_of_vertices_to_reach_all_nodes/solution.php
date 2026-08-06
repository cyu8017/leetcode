<?php

class Solution {
    /**
     * @param Integer $n
     * @param Integer[][] $edges
     * @return Integer[]
     */
    function findSmallestSetOfVertices($n, $edges) {
        $incoming = [];
        foreach ($edges as $edge) {
            $incoming[$edge[1]] = true;
        }
        $result = [];
        for ($v = 0; $v < $n; $v++) {
            if (!isset($incoming[$v])) {
                $result[] = $v;
            }
        }
        return $result;
    }
}
