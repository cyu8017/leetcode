<?php
// LeetCode 3408 - Design Task Manager
// https://leetcode.com/problems/design-task-manager/

class TaskManager {
    public $pri;
    public $user;
    public $h;

    function __construct($tasks) {
        $this->pri = [];
        $this->user = [];
        $this->h = [];
        foreach ($tasks as $t) $this->add($t[0], $t[1], $t[2]);
    }

    function add($userId, $taskId, $priority) {
        $this->pri[$taskId] = $priority;
        $this->user[$taskId] = $userId;
        $this->h[] = [$priority, $taskId, $userId];
    }

    function edit($taskId, $newPriority) {
        $this->pri[$taskId] = $newPriority;
        $this->h[] = [$newPriority, $taskId, $this->user[$taskId]];
    }

    function rmv($taskId) {
        unset($this->pri[$taskId]);
        unset($this->user[$taskId]);
    }

    function execTop() {
        usort($this->h, function($a, $b) {
            if ($a[0] !== $b[0]) return $a[0] <=> $b[0];
            return $a[1] <=> $b[1];
        });
        while (count($this->h)) {
            $top = array_pop($this->h);
            $p = $this->pri[$top[1]] ?? null;
            if ($p !== null && $p === $top[0] && ($this->user[$top[1]] ?? null) === $top[2]) {
                unset($this->pri[$top[1]]);
                $uid = $this->user[$top[1]];
                unset($this->user[$top[1]]);
                return $uid;
            }
        }
        return -1;
    }
}
