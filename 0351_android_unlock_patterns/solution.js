// LeetCode 0351 - Android Unlock Patterns
var numberOfPatterns = function(m, n) {
    const jumps = {
        "0,2": 1, "2,0": 1, "0,6": 3, "6,0": 3, "0,8": 4, "8,0": 4,
        "2,8": 5, "8,2": 5, "2,6": 7, "6,2": 7, "6,8": 7, "8,6": 7,
        "1,7": 8, "7,1": 8, "3,7": 6, "7,3": 6, "1,5": 4, "5,1": 4,
        "3,5": 5, "5,3": 5, "1,3": 2, "3,1": 2, "4,5": 5, "5,4": 5,
        "4,7": 8, "7,4": 8, "4,3": 5, "3,4": 5, "4,1": 2, "1,4": 2,
        "4,6": 7, "6,4": 7, "4,8": 6, "8,4": 6, "4,0": 2, "0,4": 2,
        "4,2": 6, "2,4": 6,
    };

    const isValid = (visited, last, nextCell) => {
        if (visited & (1 << nextCell)) return false;
        const key = `${last},${nextCell}`;
        if (key in jumps) return !(visited & (1 << jumps[key]));
        return Math.abs(Math.floor(last / 3) - Math.floor(nextCell / 3)) <= 1
            && Math.abs((last % 3) - (nextCell % 3)) <= 1;
    };

    const dfs = (visited, last, length) => {
        if (length > n) return 0;
        let count = length >= m && length <= n ? 1 : 0;
        for (let nextCell = 0; nextCell < 9; nextCell += 1) {
            if (isValid(visited, last, nextCell)) {
                count += dfs(visited | (1 << nextCell), nextCell, length + 1);
            }
        }
        return count;
    };

    return dfs(1 << 0, 0, 1) * 4 + dfs(1 << 1, 1, 1) * 4 + dfs(1 << 4, 4, 1);
};
