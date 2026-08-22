// LeetCode 1801 - Number of Orders in the Backlog
// https://leetcode.com/problems/number-of-orders-in-the-backlog/

function getNumberOfBacklogOrders(orders: number[][]): number {
    const MOD = 1e9 + 7;
    const buy: number[][] = [];
    const sell: number[][] = [];

    const pushBuy = (price: number, amount: number): void => {
        buy.push([-price, amount]);
        let i = buy.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (buy[p][0] <= buy[i][0]) break;
            [buy[p], buy[i]] = [buy[i], buy[p]];
            i = p;
        }
    };
    const pushSell = (price: number, amount: number): void => {
        sell.push([price, amount]);
        let i = sell.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (sell[p][0] <= sell[i][0]) break;
            [sell[p], sell[i]] = [sell[i], sell[p]];
            i = p;
        }
    };
    const popBuy = (): number[] => {
        const top = buy[0];
        const last = buy.pop()!;
        if (buy.length === 0) return top;
        buy[0] = last;
        let i = 0;
        const n = buy.length;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < n && buy[l][0] < buy[s][0]) s = l;
            if (r < n && buy[r][0] < buy[s][0]) s = r;
            if (s === i) break;
            [buy[s], buy[i]] = [buy[i], buy[s]];
            i = s;
        }
        return top;
    };
    const popSell = (): number[] => {
        const top = sell[0];
        const last = sell.pop()!;
        if (sell.length === 0) return top;
        sell[0] = last;
        let i = 0;
        const n = sell.length;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < n && sell[l][0] < sell[s][0]) s = l;
            if (r < n && sell[r][0] < sell[s][0]) s = r;
            if (s === i) break;
            [sell[s], sell[i]] = [sell[i], sell[s]];
            i = s;
        }
        return top;
    };

    for (const [price, amount, orderType] of orders) {
        if (orderType === 0) pushBuy(price, amount);
        else pushSell(price, amount);

        while (buy.length && sell.length && -buy[0][0] >= sell[0][0]) {
            let [negBuyPrice, buyAmount] = popBuy();
            let [sellPrice, sellAmount] = popSell();
            const matched = Math.min(buyAmount, sellAmount);
            buyAmount -= matched;
            sellAmount -= matched;
            if (buyAmount) pushBuy(-negBuyPrice, buyAmount);
            if (sellAmount) pushSell(sellPrice, sellAmount);
        }
    }

    let total = 0;
    for (const [, amount] of buy) total = (total + amount) % MOD;
    for (const [, amount] of sell) total = (total + amount) % MOD;
    return total;
}
