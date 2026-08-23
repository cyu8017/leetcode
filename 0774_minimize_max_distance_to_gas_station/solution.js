// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

/**
 * @param {number[]} stations
 * @param {number} k
 * @return {number}
 */
var minmaxGasDist = function(stations, k) {
    const can = (dist) => {
        let needed = 0;
        for (let i = 1; i < stations.length; i++)
            needed += Math.floor((stations[i] - stations[i - 1]) / dist);
        return needed <= k;
    };
    let lo = 0.0, hi = stations[stations.length - 1] - stations[0];
    while (hi - lo > 1e-6) {
        const mid = (lo + hi) / 2.0;
        if (can(mid)) hi = mid;
        else lo = mid;
    }
    return hi;
};
