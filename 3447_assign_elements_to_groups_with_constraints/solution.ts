// LeetCode 3447 - Assign Elements to Groups with Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

export function assignElements(groups: any, elements: any): any {
    const maxV = 100001;
    const first = new Array(maxV).fill(-1);
    for (let i = 0; i < elements.length; i++) {
        const e = elements[i];
        if (e < maxV && first[e] === -1) first[e] = i;
    }
    const ans = new Array(groups.length);
    for (let gi = 0; gi < groups.length; gi++) {
        const g = groups[gi];
        let best = -1;
        for (let d = 1; d * d <= g; d++) {
            if (g % d === 0) {
                if (first[d] !== -1 && (best === -1 || first[d] < best)) best = first[d];
                const other = Math.floor(g / d);
                if (first[other] !== -1 && (best === -1 || first[other] < best)) best = first[other];
            }
        }
        ans[gi] = best;
    }
    return ans;
}
