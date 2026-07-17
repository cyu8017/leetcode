<?php
// LeetCode 1797 - Design Authentication Manager
// https://leetcode.com/problems/design-authentication-manager/

class AuthenticationManager {
    private $ttl;
    private $tokens = [];

    /**
     * @param Integer $timeToLive
     */
    function __construct($timeToLive) {
        $this->ttl = $timeToLive;
    }

    /**
     * @param String $tokenId
     * @param Integer $currentTime
     * @return NULL
     */
    function generate($tokenId, $currentTime) {
        $this->tokens[$tokenId] = $currentTime + $this->ttl;
    }

    /**
     * @param String $tokenId
     * @param Integer $currentTime
     * @return NULL
     */
    function renew($tokenId, $currentTime) {
        if (isset($this->tokens[$tokenId]) && $this->tokens[$tokenId] > $currentTime) {
            $this->tokens[$tokenId] = $currentTime + $this->ttl;
        }
    }

    /**
     * @param Integer $currentTime
     * @return Integer
     */
    function countUnexpiredTokens($currentTime) {
        $count = 0;
        foreach ($this->tokens as $exp) {
            if ($exp > $currentTime) $count++;
        }
        return $count;
    }
}
