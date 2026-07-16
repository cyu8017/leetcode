// LeetCode 0483 - Smallest Good Base
// https://leetcode.com/problems/smallest-good-base/

class Solution {
    smallestGoodBase(n) {
        const num = BigInt(n);
        for (let length = BigInt(Math.floor(Math.log2(Number(num))) + 1); length > 1n; length -= 1n) {
            let low = 2n;
            let high = num - 1n;
            while (low <= high) {
                const mid = (low + high) / 2n;
                let total = 1n;
                let power = 1n;
                let ok = true;
                for (let step = 1n; step < length; step += 1n) {
                    power *= mid;
                    total += power;
                    if (total > num) {
                        ok = false;
                        break;
                    }
                }
                if (ok && total === num) return mid.toString();
                if (!ok || total > num) high = mid - 1n;
                else low = mid + 1n;
            }
        }
        return (num - 1n).toString();
    }
}

module.exports = { Solution };
