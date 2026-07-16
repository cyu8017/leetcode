// LeetCode 0386 - Lexicographical Numbers
var lexicalOrder = function (n) {
    const result = [];

    function dfs(current) {
        if (current > n) return;
        result.push(current);
        dfs(current * 10);
        if (current % 10 < 9) dfs(current + 1);
    }

    dfs(1);
    return result;
};

module.exports = { lexicalOrder };
