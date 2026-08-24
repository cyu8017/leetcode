// LeetCode 3704 - Count No-Zero Pairs That Sum to N
// https://leetcode.com/problems/count-no-zero-pairs-that-sum-to-n/

export function countNoZeroPairs(n: any): any {
    const s = String(n);
    const m = s.length;
    const digits = new Array(m + 1).fill(0);
    for (let i = 0; i < m; i++) digits[i] = s.charCodeAt(m - 1 - i) - 48;
    let dp = Array.from({length: 2}, () => Array.from({length: 2}, () => [0, 0]));
    dp[0][1][1] = 1;
    for (let pos = 0; pos < m + 1; pos++) {
        const ndp = Array.from({length: 2}, () => Array.from({length: 2}, () => [0, 0]));
        const target = digits[pos];
        for (let carry = 0; carry <= 1; carry++) {
            for (let aliveA = 0; aliveA <= 1; aliveA++) {
                for (let aliveB = 0; aliveB <= 1; aliveB++) {
                    const ways = dp[carry][aliveA][aliveB];
                    if (ways === 0) continue;
                    const A = [];
                    if (aliveA === 1) {
                        for (let d = 1; d <= 9; d++) A.push([d, 1]);
                        if (pos > 0) A.push([0, 0]);
                    } else {
                        A.push([0, 0]);
                    }
                    const B = [];
                    if (aliveB === 1) {
                        for (let d = 1; d <= 9; d++) B.push([d, 1]);
                        if (pos > 0) B.push([0, 0]);
                    } else {
                        B.push([0, 0]);
                    }
                    for (const [da, na] of A) {
                        for (const [db, nb] of B) {
                            const sum = da + db + carry;
                            if (sum % 10 !== target) continue;
                            const ncarry = Math.floor(sum / 10);
                            ndp[ncarry][na][nb] += ways;
                        }
                    }
                }
            }
        }
        dp = ndp;
    }
    return dp[0][0][0];
}
