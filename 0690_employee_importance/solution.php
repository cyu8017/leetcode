<?php
// LeetCode 0690 - Employee Importance
// https://leetcode.com/problems/employee-importance/

class Employee {
    public $id;
    public $importance;
    public $subordinates;
    function __construct($id = 0, $importance = 0, $subordinates = []) {
        $this->id = $id;
        $this->importance = $importance;
        $this->subordinates = $subordinates;
    }
}

class Solution {
    function getImportance($employees, $id) {
        $table = [];
        foreach ($employees as $emp) {
            if (is_array($emp)) {
                $eid = $emp[0];
                $imp = $emp[1];
                $subs = $emp[2];
            } else {
                $eid = $emp->id;
                $imp = $emp->importance;
                $subs = $emp->subordinates;
            }
            $table[$eid] = [$imp, $subs];
        }
        $dfs = function ($eid) use (&$dfs, &$table) {
            [$imp, $subs] = $table[$eid];
            $total = $imp;
            foreach ($subs as $sub) $total += $dfs($sub);
            return $total;
        };
        return $dfs($id);
    }
}
