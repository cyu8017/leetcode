<?php
// LeetCode 2590 - Design a Todo List
// https://leetcode.com/problems/design-a-todo-list/

class TodoList {
    private $nextID;
    private $tasks;
    private $users;

    function __construct() {
        $this->nextID = 1;
        $this->tasks = [];
        $this->users = [];
    }

    function addTask($userId, $taskDescription, $dueDate, $tags) {
        $id = $this->nextID++;
        $tagSet = [];
        foreach ($tags as $tag) $tagSet[$tag] = true;
        $this->tasks[$id] = [
            'id' => $id,
            'description' => $taskDescription,
            'dueDate' => $dueDate,
            'userId' => $userId,
            'tags' => $tagSet,
            'done' => false,
        ];
        if (!isset($this->users[$userId])) $this->users[$userId] = [];
        $this->users[$userId][] = $id;
        return $id;
    }

    function getAllTasks($userId) {
        if (!isset($this->users[$userId])) return [];
        $ids = $this->users[$userId];
        usort($ids, function($a, $b) {
            return $this->tasks[$a]['dueDate'] <=> $this->tasks[$b]['dueDate'];
        });
        $ans = [];
        foreach ($ids as $id) {
            if (!$this->tasks[$id]['done']) $ans[] = $this->tasks[$id]['description'];
        }
        return $ans;
    }

    function getTasksForTag($userId, $tag) {
        if (!isset($this->users[$userId])) return [];
        $ids = $this->users[$userId];
        usort($ids, function($a, $b) {
            return $this->tasks[$a]['dueDate'] <=> $this->tasks[$b]['dueDate'];
        });
        $ans = [];
        foreach ($ids as $id) {
            $tk = $this->tasks[$id];
            if (!$tk['done'] && isset($tk['tags'][$tag])) $ans[] = $tk['description'];
        }
        return $ans;
    }

    function completeTask($userId, $taskId) {
        if (!isset($this->tasks[$taskId])) return;
        $tk = &$this->tasks[$taskId];
        if ($tk['userId'] !== $userId || $tk['done']) return;
        $tk['done'] = true;
    }
}
