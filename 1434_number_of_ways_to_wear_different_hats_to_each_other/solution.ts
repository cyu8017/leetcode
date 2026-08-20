function numberWays(hats: any): any {
    const mod = 1000000007, n = hats.length, owners = Array.from({length: 41}, (: any): any => []);
    hats.forEach((list, person: any): any => list.forEach((hat: any): any => owners[hat].push(person)));
    const memo = new Map();
    const dfs = (hat: any, mask: any): any => {
        if (mask === (1 << n) - 1) return 1;
        if (hat > 40) return 0;
        const key = hat + "," + mask; if (memo.has(key)) return memo.get(key);
        let ways = dfs(hat + 1, mask);
        for (const person of owners[hat]) if (!(mask & (1 << person))) ways = (ways + dfs(hat + 1, mask | (1 << person))) % mod;
        memo.set(key, ways); return ways;
    };
    return dfs(1, 0);
}
