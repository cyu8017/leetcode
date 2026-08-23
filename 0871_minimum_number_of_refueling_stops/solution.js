// LeetCode 0871 - Minimum Number of Refueling Stops
// https://leetcode.com/problems/minimum-number-of-refueling-stops/

/**
 * @param {number} target
 * @param {number} startFuel
 * @param {number[][]} stations
 * @return {number}
 */
var minRefuelStops = function(target, startFuel, stations) {
    const pq = [];
    const push = (gas) => {
        pq.push(gas);
        let i = pq.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (pq[i] <= pq[p]) break;
            [pq[i], pq[p]] = [pq[p], pq[i]];
            i = p;
        }
    };
    const pop = () => {
        const top = pq[0];
        const last = pq.pop();
        if (pq.length) {
            pq[0] = last;
            let i = 0;
            while (true) {
                let largest = i;
                const l = i * 2 + 1, r = i * 2 + 2;
                if (l < pq.length && pq[l] > pq[largest]) largest = l;
                if (r < pq.length && pq[r] > pq[largest]) largest = r;
                if (largest === i) break;
                [pq[i], pq[largest]] = [pq[largest], pq[i]];
                i = largest;
            }
        }
        return top;
    };
    const all = stations.concat([[target, 0]]);
    let ans = 0, prev = 0, fuel = startFuel;
    for (const [pos, gas] of all) {
        fuel -= pos - prev;
        while (pq.length && fuel < 0) {
            fuel += pop();
            ans++;
        }
        if (fuel < 0) return -1;
        push(gas);
        prev = pos;
    }
    return ans;
};
