// LeetCode 1535 - Find the Winner of an Array Game
// https://leetcode.com/problems/find-the-winner-of-an-array-game/

/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var getWinner = function(arr, k) {
    let champion = arr[0], wins = 0;
    for (let i = 1; i < arr.length; i++) {
        if (champion > arr[i]) wins++;
        else { champion = arr[i]; wins = 1; }
        if (wins === k) break;
    }
    return champion;
};
