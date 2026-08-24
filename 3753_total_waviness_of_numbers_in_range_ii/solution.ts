// LeetCode 3753 - Total Waviness Of Numbers In Range Ii
// https://leetcode.com/problems/total_waviness_of_numbers_in_range_ii/

export function totalWaviness(a: any, b: any): any {
    const wavinessUpTo = (limit) => {
        if (limit < 0) return 0;
        const digits = [];
        if (limit === 0) digits.push(0);
        else {
            for (let value = limit; value > 0; value = Math.floor(value / 10))
                digits.push(value % 10);
            digits.reverse();
        }
        const memo = new Map();
        const dfs = (position, secondLast, last, started, tight) => {
            if (position === digits.length) return {count: 1, sum: 0};
            const key = position + "," + secondLast + "," + last + "," + started;
            if (!tight && memo.has(key)) return memo.get(key);
            const upper = tight ? digits[position] : 9;
            const result = {count: 0, sum: 0};
            for (let digit = 0; digit <= upper; digit++) {
                const nextTight = tight && digit === upper;
                let nextSecondLast = secondLast, nextLast = last;
                const nextStarted = started || digit !== 0;
                let add = 0;
                if (!nextStarted) {
                    nextSecondLast = nextLast = 10;
                } else if (!started) {
                    nextSecondLast = 10;
                    nextLast = digit;
                } else {
                    if (secondLast !== 10 &&
                        ((last > secondLast && last > digit) || (last < secondLast && last < digit))) {
                        add = 1;
                    }
                    nextSecondLast = last;
                    nextLast = digit;
                }
                const child = dfs(position + 1, nextSecondLast, nextLast, nextStarted, nextTight);
                result.count += child.count;
                result.sum += child.sum + add * child.count;
            }
            if (!tight) memo.set(key, result);
            return result;
        };
        return dfs(0, 10, 10, false, true).sum;
    };
    return wavinessUpTo(b) - wavinessUpTo(a - 1);
}
