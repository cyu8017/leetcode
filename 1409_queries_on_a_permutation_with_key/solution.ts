// LeetCode 1409: Queries On A Permutation With Key

function processQueries(queries: any, m: any): any {
    const permutation = Array.from({ length: m }, (_, i: any): any => i + 1);
    return queries.map((query: any): any => { const index = permutation.indexOf(query); permutation.splice(index, 1); permutation.unshift(query); return index; });
}
