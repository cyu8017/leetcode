<?php
// LeetCode 2408 - Design SQL
// https://leetcode.com/problems/design-sql/

class SQL {
    private $tables;
    private $nextID;

    function __construct($names, $columns) {
        $this->tables = [];
        $this->nextID = [];
        foreach ($names as $name) {
            $this->tables[$name] = [];
            $this->nextID[$name] = 1;
        }
    }

    function ins($name, $row) {
        if (!isset($this->tables[$name])) return false;
        $id = $this->nextID[$name];
        $this->nextID[$name] = $id + 1;
        $full = array_merge([strval($id)], $row);
        $this->tables[$name][] = $full;
        return true;
    }

    function rmv($name, $rowId) {
        if (!isset($this->tables[$name])) return;
        $rows = &$this->tables[$name];
        $n = count($rows);
        for ($i = 0; $i < $n; $i++) {
            if (intval($rows[$i][0]) === $rowId) {
                array_splice($rows, $i, 1);
                return;
            }
        }
    }

    function sel($name, $rowId, $columnId) {
        if (!isset($this->tables[$name])) return "<null>";
        foreach ($this->tables[$name] as $r) {
            if (intval($r[0]) === $rowId) {
                if ($columnId < 1 || $columnId >= count($r)) return "<null>";
                return $r[$columnId];
            }
        }
        return "<null>";
    }

    function exp($name) {
        $ans = [];
        foreach ($this->tables[$name] ?? [] as $r) {
            $ans[] = implode(',', $r);
        }
        return $ans;
    }
}
