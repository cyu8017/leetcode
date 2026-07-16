// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

class Solution {
    findMaximizedCapital(k, w, profits, capital) {
        const projects = capital.map((cap, index) => [cap, profits[index]]).sort((a, b) => a[0] - b[0]);
        const available = [];
        let index = 0;
        for (let round = 0; round < k; round += 1) {
            while (index < projects.length && projects[index][0] <= w) {
                available.push(-projects[index][1]);
                available.sort((a, b) => a - b);
                index += 1;
            }
            if (!available.length) break;
            w -= available.shift();
        }
        return w;
    }
}

module.exports = { Solution };
