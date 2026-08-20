// LeetCode 1169 - Invalid Transactions
// https://leetcode.com/problems/invalid-transactions/

function invalidTransactions(transactions: string[]): string[] {
    const parsed = transactions.map((t) => {
        const [name, time, amount, city] = t.split(",");
        return [name, +time, +amount, city, t];
    });
    const invalid = new Set();
    for (let i = 0; i < parsed.length; i++) {
        const [name, time, amount, city, raw] = parsed[i];
        if (amount > 1000) invalid.add(raw);
        for (let j = 0; j < parsed.length; j++) {
            if (i === j) continue;
            const [name2, time2, , city2, raw2] = parsed[j];
            if (name === name2 && city !== city2 && Math.abs(time - time2) <= 60) {
                invalid.add(raw);
                invalid.add(raw2);
            }
        }
    }
    return [...invalid];
}
