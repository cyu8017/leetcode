// LeetCode 0842 - Split Array into Fibonacci Sequence
// https://leetcode.com/problems/split-array-into-fibonacci-sequence/

export function splitIntoFibonacci(num: string): number[] {
    const path = [];
    const dfs = (start) => {
        const n = num.length;
        if (start === n) return path.length >= 3;
        let val = 0;
        for (let end = start; end < n; end++) {
            if (num[start] === '0' && end > start) break;
            val = val * 10 + (num.charCodeAt(end) - 48);
            if (val > 2147483647) break;
            if (path.length >= 2) {
                const total = path[path.length - 1] + path[path.length - 2];
                if (val < total) continue;
                if (val > total) break;
            }
            path.push(val);
            if (dfs(end + 1)) return true;
            path.pop();
        }
        return false;
    };
    dfs(0);
    return path;
}
