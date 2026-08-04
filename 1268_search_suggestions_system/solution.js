// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

/**
 * @param {string[]} products
 * @param {string} searchWord
 * @return {string[][]}
 */
var suggestedProducts = function(products, searchWord) {
    products.sort();
    const answer = [];
    let prefix = '';
    for (const ch of searchWord) {
        prefix += ch;
        let lo = 0;
        let hi = products.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (products[mid] < prefix) lo = mid + 1;
            else hi = mid;
        }
        const row = [];
        for (let i = lo; i < products.length && row.length < 3; i++) {
            if (products[i].startsWith(prefix)) row.push(products[i]);
            else break;
        }
        answer.push(row);
    }
    return answer;
};
