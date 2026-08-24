// LeetCode 2910 - Minimum Number of Groups to Create a Valid Assignment
// https://leetcode.com/problems/minimum-number-of-groups-to-create-a-valid-assignment/

export function minGroupsForValidAssignment(balls: number[]): number {
    const freq = new Map();
    for (const b of balls) freq.set(b, (freq.get(b) || 0) + 1);
    const counts = [...freq.values()];
    let minF = Math.min(...counts);
    for (let size = minF; size >= 1; size--) {
        let ok = true, groups = 0;
        for (const c of counts) {
            const rem = c % (size + 1);
            const g2 = Math.floor(c / (size + 1));
            if (rem === 0) groups += g2;
            else if (size - rem <= g2) groups += g2 + 1;
            else { ok = false; break; }
        }
        if (ok) return groups;
    }
    return balls.length;
}
