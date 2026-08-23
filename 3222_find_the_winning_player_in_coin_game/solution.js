// LeetCode 3222 - Find the Winning Player in Coin Game
// https://leetcode.com/problems/find-the-winning-player-in-coin-game/

var losingPlayer = function(x, y) {
    let k = Math.min(Math.floor(x / 2), Math.floor(y / 8));
    x -= 2 * k;
    y -= 8 * k;
    if (x > 0 && y >= 4) return "Alice";
    return "Bob";
};
