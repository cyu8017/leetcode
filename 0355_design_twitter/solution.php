<?php
// LeetCode 0355 - Design Twitter
// https://leetcode.com/problems/design-twitter/

class Twitter {
    private int $time = 0;
    /** @var array<int, array<int, array{0: int, 1: int}>> */
    private array $tweets = [];
    /** @var array<int, array<int, bool>> */
    private array $following = [];

    function postTweet(int $userId, int $tweetId): void {
        $this->post_tweet($userId, $tweetId);
    }

    function post_tweet(int $userId, int $tweetId): void {
        $this->time++;
        if (!array_key_exists($userId, $this->tweets)) {
            $this->tweets[$userId] = [];
        }
        $this->tweets[$userId][] = [$this->time, $tweetId];
    }

    /**
     * @return Integer[]
     */
    function getNewsFeed(int $userId): array {
        return $this->get_news_feed($userId);
    }

    /**
     * @return Integer[]
     */
    function get_news_feed(int $userId): array {
        $users = array_keys($this->following[$userId] ?? []);
        $users[] = $userId;
        $candidates = [];

        foreach ($users as $uid) {
            $recent = array_slice($this->tweets[$uid] ?? [], -10);
            foreach ($recent as $entry) {
                $candidates[] = $entry;
            }
        }

        usort($candidates, function ($left, $right) {
            return $right[0] <=> $left[0];
        });

        $feed = [];
        foreach ($candidates as $entry) {
            $feed[] = $entry[1];
            if (count($feed) === 10) {
                break;
            }
        }

        return $feed;
    }

    function follow(int $followerId, int $followeeId): void {
        if (!array_key_exists($followerId, $this->following)) {
            $this->following[$followerId] = [];
        }
        $this->following[$followerId][$followeeId] = true;
    }

    function unfollow(int $followerId, int $followeeId): void {
        unset($this->following[$followerId][$followeeId]);
    }
}
