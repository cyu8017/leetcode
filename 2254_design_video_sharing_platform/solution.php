<?php
// LeetCode 2254 - Design Video Sharing Platform
// https://leetcode.com/problems/design-video-sharing-platform/

class VideoSharingPlatform {
    private $nextID = 0;
    private $free;
    private $videos = [];
    private $views = [];
    private $likes = [];
    private $dislikes = [];

    function __construct() {
        $this->free = new SplPriorityQueue();
    }

    function upload($video) {
        if (!$this->free->isEmpty()) $id = $this->free->extract();
        else $id = $this->nextID++;
        $this->videos[$id] = $video;
        $this->views[$id] = 0;
        $this->likes[$id] = 0;
        $this->dislikes[$id] = 0;
        return $id;
    }

    function remove($videoId) {
        if (!isset($this->videos[$videoId])) return;
        unset($this->videos[$videoId], $this->views[$videoId], $this->likes[$videoId], $this->dislikes[$videoId]);
        $this->free->insert($videoId, -$videoId);
    }

    function watch($videoId, $startMinute, $endMinute) {
        if (!isset($this->videos[$videoId])) return '-1';
        $v = $this->videos[$videoId];
        $this->views[$videoId]++;
        if ($startMinute >= strlen($v)) return '';
        $endMinute = min($endMinute, strlen($v) - 1);
        return substr($v, $startMinute, $endMinute - $startMinute + 1);
    }

    function like($videoId) {
        if (isset($this->videos[$videoId])) $this->likes[$videoId]++;
    }

    function dislike($videoId) {
        if (isset($this->videos[$videoId])) $this->dislikes[$videoId]++;
    }

    function getLikesAndDislikes($videoId) {
        if (!isset($this->videos[$videoId])) return [-1];
        return [$this->likes[$videoId], $this->dislikes[$videoId]];
    }

    function getViews($videoId) {
        if (!isset($this->videos[$videoId])) return -1;
        return $this->views[$videoId];
    }
}
