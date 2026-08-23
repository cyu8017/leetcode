// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

/**
 * @param {number[][]} graph
 * @return {number}
 */
var catMouseGame = function(graph) {
    const n = graph.length;
    const DRAW = 0, MOUSE_WIN = 1, CAT_WIN = 2;
    const states = Array.from({ length: n }, () => Array.from({ length: n }, () => [0, 0]));
    const outDegree = Array.from({ length: n }, () => Array.from({ length: n }, () => [0, 0]));
    const q = [];
    for (let cat = 0; cat < n; cat++) {
        for (let mouse = 0; mouse < n; mouse++) {
            outDegree[cat][mouse][0] = graph[mouse].length;
            let deg = 0;
            for (const x of graph[cat]) if (x !== 0) deg++;
            outDegree[cat][mouse][1] = deg;
        }
    }
    for (let cat = 1; cat < n; cat++) {
        for (let move = 0; move < 2; move++) {
            states[cat][0][move] = MOUSE_WIN;
            q.push([cat, 0, move, MOUSE_WIN]);
            states[cat][cat][move] = CAT_WIN;
            q.push([cat, cat, move, CAT_WIN]);
        }
    }
    while (q.length) {
        const [cat, mouse, move, state] = q.shift();
        if (cat === 2 && mouse === 1 && move === 0) return state;
        const prevMove = move ^ 1;
        for (const prev of graph[prevMove === 1 ? cat : mouse]) {
            const prevCat = prevMove === 1 ? prev : cat;
            if (prevCat === 0) continue;
            const prevMouse = prevMove === 1 ? mouse : prev;
            if (states[prevCat][prevMouse][prevMove] !== 0) continue;
            if ((prevMove === 0 && state === MOUSE_WIN) ||
                (prevMove === 1 && state === CAT_WIN) ||
                outDegree[prevCat][prevMouse][prevMove] === 1) {
                states[prevCat][prevMouse][prevMove] = state;
                q.push([prevCat, prevMouse, prevMove, state]);
            } else {
                outDegree[prevCat][prevMouse][prevMove]--;
            }
        }
    }
    return states[2][1][0];
};
