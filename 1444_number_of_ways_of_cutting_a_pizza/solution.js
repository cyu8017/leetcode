var ways = function(pizza, k) {
    const mod = 1000000007, m = pizza.length, n = pizza[0].length, apples = Array.from({length:m+1}, () => Array(n+1).fill(0));
    for (let r = m - 1; r >= 0; r--) for (let c = n - 1; c >= 0; c--) apples[r][c] = (pizza[r][c] === "A") + apples[r+1][c] + apples[r][c+1] - apples[r+1][c+1];
    const memo = new Map(), dfs = (r, c, cuts) => { if (apples[r][c] === 0) return 0; if (cuts === 1) return 1; const key = r+","+c+","+cuts; if (memo.has(key)) return memo.get(key); let result = 0; for (let x=r+1;x<m;x++) if (apples[r][c]-apples[x][c]>0) result=(result+dfs(x,c,cuts-1))%mod; for (let y=c+1;y<n;y++) if(apples[r][c]-apples[r][y]>0) result=(result+dfs(r,y,cuts-1))%mod; memo.set(key,result); return result; };
    return dfs(0, 0, k);
};
