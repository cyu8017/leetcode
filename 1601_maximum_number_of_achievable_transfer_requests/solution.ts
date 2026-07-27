// LeetCode 1601 - Maximum Number of Achievable Transfer Requests
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

function maximumRequests(n: number, requests: number[][]): number {
    let ans = 0;
    const m = requests.length;
    for (let mask = 0; mask < (1 << m); mask++) {
        const bits = mask.toString(2).split("1").length - 1;
        if (bits <= ans) continue;
        const bal = Array(n).fill(0);
        for (let i = 0; i < m; i++) {
            if ((mask >> i) & 1) {
                bal[requests[i][0]]--;
                bal[requests[i][1]]++;
            }
        }
        if (bal.every((x) => x === 0)) ans = bits;
    }
    return ans;
}
