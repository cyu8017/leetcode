// LeetCode 1849 - Splitting a String Into Descending Consecutive Values
// https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

function splitString(s: string): boolean {
    const n = s.length;
    const dfs = (index: number, previous: bigint | null, parts: number): boolean => {
        if (index === n) return parts >= 2;
        for (let end = index + 1; end <= n; end++) {
            const value = BigInt(s.slice(index, end));
            if (previous === null) {
                if (dfs(end, value, parts + 1)) return true;
            } else if (value === previous - 1n) {
                if (dfs(end, value, parts + 1)) return true;
            } else if (value > previous - 1n) {
                break;
            }
        }
        return false;
    };
    return dfs(0, null, 0);
}
