"use strict";
// LeetCode 1884 - Egg Drop With 2 Eggs and N Floors
// https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/
function twoEggDrop(n) {
    let moves = 0, covered = 0;
    while (covered < n) {
        moves++;
        covered += moves;
    }
    return moves;
}
