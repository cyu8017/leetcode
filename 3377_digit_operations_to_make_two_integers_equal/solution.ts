// LeetCode 3377 - Digit Operations to Make Two Integers Equal
// https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/

function sieve(n: any): any {
    const isP = new Array(n).fill(false);
    for (let i = 2; i < n; i++) isP[i] = true;
    for (let i = 2; i * i < n; i++) {
        if (isP[i]) {
            for (let j = i * i; j < n; j += i) isP[j] = false;
        }
    }
    return isP;
}export function minOperations(n: any, m: any): any {
    const isPrime = sieve(100000);
    if (isPrime[n]) return -1;
    const dist = new Array(100000).fill(-1);
    const pq = [[n, n]];
    dist[n] = n;
    while (pq.length) {
        pq.sort((a, b) => a[0] - b[0]);
        const cur = pq.shift();
        const cost = cur[0], val = cur[1];
        if (cost !== dist[val]) continue;
        if (val === m) return cost;
        const s = String(val).split('');
        for (let i = 0; i < s.length; i++) {
            const orig = s[i];
            for (const d of [-1, 1]) {
                const nd = (orig.charCodeAt(0) - 48) + d;
                if (nd < 0 || nd > 9) continue;
                if (i === 0 && nd === 0 && s.length > 1) continue;
                s[i] = String(nd);
                const nv = parseInt(s.join(''), 10);
                s[i] = orig;
                if (isPrime[nv]) continue;
                const nc = cost + nv;
                if (dist[nv] === -1 || nc < dist[nv]) {
                    dist[nv] = nc;
                    pq.push([nc, nv]);
                }
            }
        }
    }
    return -1;
}
