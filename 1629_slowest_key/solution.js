// LeetCode 1629 - Slowest Key
// https://leetcode.com/problems/slowest-key/

/**
 * @param {number[]} releaseTimes
 * @param {string} keysPressed
 * @return {character}
 */
var slowestKey = function(releaseTimes, keysPressed) {
    let bestDur = releaseTimes[0], bestKey = keysPressed[0];
    for (let i = 1; i < releaseTimes.length; i++) {
        const duration = releaseTimes[i] - releaseTimes[i - 1];
        if (duration > bestDur || (duration === bestDur && keysPressed[i] > bestKey)) {
            bestDur = duration;
            bestKey = keysPressed[i];
        }
    }
    return bestKey;
};
