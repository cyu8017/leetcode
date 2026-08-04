var isPathCrossing = function(path) {
    let x = 0, y = 0;
    const visited = new Set(['0,0']);
    const moves = { N: [0, 1], S: [0, -1], E: [1, 0], W: [-1, 0] };
    for (const direction of path) {
        x += moves[direction][0];
        y += moves[direction][1];
        const location = `${x},${y}`;
        if (visited.has(location)) return true;
        visited.add(location);
    }
    return false;
};
