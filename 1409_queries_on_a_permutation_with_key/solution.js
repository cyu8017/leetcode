// LeetCode 1409: Queries On A Permutation With Key

var processQueries = function(queries, m) {
    const permutation = Array.from({ length: m }, (_, i) => i + 1);
    return queries.map(query => { const index = permutation.indexOf(query); permutation.splice(index, 1); permutation.unshift(query); return index; });
};
