<?php
// LeetCode 1500 - Design a File Sharing System
// https://leetcode.com/problems/design-a-file-sharing-system/

class FileSharing {
    private $owners = [];
    private $chunks = [];
    private $free;
    private $nextId = 1;

    /**
     * @param Integer $m
     */
    function __construct($m) {
        $this->free = new SplMinHeap();
    }

    /**
     * @param Integer[] $ownedChunks
     * @return Integer
     */
    function join($ownedChunks) {
        if (!$this->free->isEmpty()) {
            $user = $this->free->extract();
        } else {
            $user = $this->nextId++;
        }
        $owned = [];
        foreach ($ownedChunks as $chunk) {
            $owned[$chunk] = true;
            if (!isset($this->owners[$chunk])) {
                $this->owners[$chunk] = [];
            }
            $this->owners[$chunk][$user] = true;
        }
        $this->chunks[$user] = $owned;
        return $user;
    }

    /**
     * @param Integer $userID
     * @return NULL
     */
    function leave($userID) {
        if (!isset($this->chunks[$userID])) {
            return;
        }
        foreach (array_keys($this->chunks[$userID]) as $chunk) {
            unset($this->owners[$chunk][$userID]);
        }
        unset($this->chunks[$userID]);
        $this->free->insert($userID);
    }

    /**
     * @param Integer $userID
     * @param Integer $chunkID
     * @return Integer[]
     */
    function request($userID, $chunkID) {
        if (empty($this->owners[$chunkID])) {
            return [];
        }
        $users = array_map('intval', array_keys($this->owners[$chunkID]));
        sort($users);
        $this->chunks[$userID][$chunkID] = true;
        $this->owners[$chunkID][$userID] = true;
        return $users;
    }
}
