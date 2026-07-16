// LeetCode 0386 - Lexicographical Numbers
export function lexicalOrder(n: number): number[] {
    const result: number[] = [];

    function dfs(current: number): void {
        if (current > n) return;
        result.push(current);
        dfs(current * 10);
        if (current % 10 < 9) dfs(current + 1);
    }

    dfs(1);
    return result;
}
