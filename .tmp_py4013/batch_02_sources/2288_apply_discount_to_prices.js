// LeetCode 2288 - Apply Discount to Prices
// https://leetcode.com/problems/apply-discount-to-prices/

var discountPrices = function(sentence, discount) {
    const parts = sentence.split(' ');
    for (let i = 0; i < parts.length; i++) {
        const part = parts[i];
        if (part.length >= 2 && part[0] === '$') {
            let ok = true;
            for (let j = 1; j < part.length; j++) {
                if (part[j] < '0' || part[j] > '9') { ok = false; break; }
            }
            if (ok) {
                const val = Number(part.slice(1));
                const price = val * (100 - discount) / 100;
                parts[i] = '$' + price.toFixed(2);
            }
        }
    }
    return parts.join(' ');
};
