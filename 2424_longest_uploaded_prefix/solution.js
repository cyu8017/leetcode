// LeetCode 2424 - Longest Uploaded Prefix
// https://leetcode.com/problems/longest-uploaded-prefix/

/**
 * @param {number} n
 */
var LUPrefix = function(n) {
    this.uploaded = Array(n + 2).fill(false);
    this.prefixLen = 0;
};

/** 
 * @param {number} video
 * @return {void}
 */
LUPrefix.prototype.upload = function(video) {
    this.uploaded[video] = true;
    while (this.uploaded[this.prefixLen + 1]) this.prefixLen++;
};

/**
 * @return {number}
 */
LUPrefix.prototype.longest = function() {
    return this.prefixLen;
};
