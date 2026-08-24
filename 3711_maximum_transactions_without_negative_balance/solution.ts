// LeetCode 3711 - Maximum Transactions Without Negative Balance
// https://leetcode.com/problems/maximum-transactions-without-negative-balance/

export function maxTransactions(transactions: any): any {
    const tm = new Map();
    let ans = transactions.length;
    let s = 0;
    const firstKey = () => {
        let mn = Infinity;
        for (const k of tm.keys()) if (k < mn) mn = k;
        return mn;
    };
    for (const x of transactions) {
        s += x;
        tm.set(x, (tm.get(x) || 0) + 1);
        while (s < 0) {
            const y = firstKey();
            s -= y;
            ans--;
            const c = tm.get(y);
            if (c === 1) tm.delete(y);
            else tm.set(y, c - 1);
        }
    }
    return ans;
}
