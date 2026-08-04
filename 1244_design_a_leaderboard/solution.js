// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

var Leaderboard = function() {
    this.scores = new Map();
};

/** 
 * @param {number} playerId
 * @param {number} score
 * @return {void}
 */
Leaderboard.prototype.addScore = function(playerId, score) {
    this.scores.set(playerId, (this.scores.get(playerId) || 0) + score);
};

/** 
 * @param {number} K
 * @return {number}
 */
Leaderboard.prototype.top = function(K) {
    return [...this.scores.values()].sort((a, b) => b - a).slice(0, K).reduce((s, v) => s + v, 0);
};

/** 
 * @param {number} playerId
 * @return {void}
 */
Leaderboard.prototype.reset = function(playerId) {
    this.scores.delete(playerId);
};
