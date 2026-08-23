// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

/**
 * @param {object[]} animals
 * @return {object[]}
 */
var findHeavyAnimals = function(animals) {
    return animals
        .filter((r) => (Array.isArray(r) ? r[3] : r.weight) > 100)
        .sort((a, b) => (Array.isArray(b) ? b[3] : b.weight) - (Array.isArray(a) ? a[3] : a.weight))
        .map((r) => (Array.isArray(r) ? { name: r[0] } : { name: r.name }));
};
