<?php
// LeetCode 0535 - Encode and Decode TinyURL
// https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec {
    /** @var array<string, string> */
    private $urlToCode = [];
    /** @var array<string, string> */
    private $codeToUrl = [];
    /** @var int */
    private $counter = 0;
    /** @var string */
    private $base = "http://tinyurl.com/";

    /**
     * @param String $longUrl
     * @return String
     */
    function encode($longUrl) {
        if (isset($this->urlToCode[$longUrl])) {
            return $this->urlToCode[$longUrl];
        }
        $code = (string)$this->counter;
        $this->counter++;
        $shortUrl = $this->base . $code;
        $this->urlToCode[$longUrl] = $shortUrl;
        $this->codeToUrl[$shortUrl] = $longUrl;
        return $shortUrl;
    }

    /**
     * @param String $shortUrl
     * @return String
     */
    function decode($shortUrl) {
        return $this->codeToUrl[$shortUrl];
    }
}
