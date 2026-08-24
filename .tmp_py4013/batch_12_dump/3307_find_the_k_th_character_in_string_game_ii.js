// LeetCode 3307 - Find the K-th Character in String Game II
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/

var kthCharacter = function(k, operations) {
    let shift = 0;
    const ops = operations.slice();
    while (ops.length) {
        const op = ops.pop();
        const half = 1n << BigInt(ops.length);
        if (BigInt(k) > half) {
            k = Number(BigInt(k) - half);
            if (op === 1) shift++;
        }
    }
    return String.fromCharCode(97 + (shift % 26));
};
