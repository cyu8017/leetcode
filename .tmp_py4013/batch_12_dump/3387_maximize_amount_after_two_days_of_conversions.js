// LeetCode 3387 - Maximize Amount After Two Days of Conversions
// https://leetcode.com/problems/maximize-amount-after-two-days-of-conversions/

function buildRateGraph(pairs, rates) {
    const g = new Map();
    for (let i = 0; i < pairs.length; i++) {
        const a = pairs[i][0], b = pairs[i][1];
        if (!g.has(a)) g.set(a, new Map());
        if (!g.has(b)) g.set(b, new Map());
        g.get(a).set(b, rates[i]);
        g.get(b).set(a, 1.0 / rates[i]);
    }
    return g;
}
function bellman(start, pairs, rates) {
    const g = buildRateGraph(pairs, rates);
    const dist = new Map();
    dist.set(start, 1.0);
    for (let it = 0; it < 100; it++) {
        let updated = false;
        for (const [from, tos] of g) {
            if (!dist.has(from) || dist.get(from) === 0) continue;
            for (const [to, rate] of tos) {
                const nv = dist.get(from) * rate;
                if (!dist.has(to) || nv > dist.get(to)) {
                    dist.set(to, nv);
                    updated = true;
                }
            }
        }
        if (!updated) break;
    }
    return dist;
}
var maxAmount = function(initialCurrency, pairs1, rates1, pairs2, rates2) {
    const amt1 = bellman(initialCurrency, pairs1, rates1);
    let ans = 1.0;
    const g2 = buildRateGraph(pairs2, rates2);
    for (const [c, a] of amt1) {
        if (a <= 0) continue;
        const dist = new Map();
        dist.set(c, a);
        let updated = true;
        for (let it = 0; it < 100 && updated; it++) {
            updated = false;
            for (const [from, tos] of g2) {
                if (!dist.has(from) || dist.get(from) === 0) continue;
                for (const [to, rate] of tos) {
                    const nv = dist.get(from) * rate;
                    if (!dist.has(to) || nv > dist.get(to)) {
                        dist.set(to, nv);
                        updated = true;
                    }
                }
            }
        }
        if (dist.has(initialCurrency) && dist.get(initialCurrency) > ans) {
            ans = dist.get(initialCurrency);
        }
    }
    return ans;
};
