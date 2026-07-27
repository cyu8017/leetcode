// LeetCode 1687 - Delivering Boxes From Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

/**
 * @param {number[][]} boxes
 * @param {number} portsCount
 * @param {number} maxBoxes
 * @param {number} maxWeight
 * @return {number}
 */
var boxDelivering = function(boxes, portsCount, maxBoxes, maxWeight) {
    const n = boxes.length;
    const w = Array(n + 1).fill(0);
    const changes = Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        w[i] = w[i - 1] + boxes[i - 1][1];
        changes[i] = changes[i - 1] + (i > 1 && boxes[i - 1][0] !== boxes[i - 2][0] ? 1 : 0);
    }
    const dp = Array(n + 1).fill(0);
    const q = [0];
    for (let i = 1; i <= n; i++) {
        while (q.length && (i - q[0] > maxBoxes || w[i] - w[q[0]] > maxWeight)) q.shift();
        const j = q[0];
        dp[i] = dp[j] + changes[i] - changes[j + 1] + 2;
        if (i < n) {
            const val = dp[i] - changes[i + 1];
            while (q.length && dp[q[q.length - 1]] - changes[q[q.length - 1] + 1] >= val) q.pop();
            q.push(i);
        }
    }
    return dp[n];
};
