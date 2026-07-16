// LeetCode 0269 - Alien Dictionary
// https://leetcode.com/problems/alien-dictionary/

/**
 * @param {string[]} words
 * @return {string}
 */
var alienOrder = function(words) {
    const graph = new Map();
    const indegree = new Map();

    for (const word of words) {
        for (const char of word) {
            if (!graph.has(char)) {
                graph.set(char, new Set());
                indegree.set(char, 0);
            }
        }
    }

    for (let i = 0; i < words.length - 1; i++) {
        const first = words[i];
        const second = words[i + 1];
        if (first.length > second.length && first.startsWith(second)) {
            return '';
        }
        for (let j = 0; j < Math.min(first.length, second.length); j++) {
            if (first[j] !== second[j]) {
                if (!graph.get(first[j]).has(second[j])) {
                    graph.get(first[j]).add(second[j]);
                    indegree.set(second[j], indegree.get(second[j]) + 1);
                }
                break;
            }
        }
    }

    const queue = [];
    for (const [char, degree] of indegree) {
        if (degree === 0) {
            queue.push(char);
        }
    }

    const order = [];
    while (queue.length) {
        const char = queue.shift();
        order.push(char);
        for (const next of graph.get(char)) {
            indegree.set(next, indegree.get(next) - 1);
            if (indegree.get(next) === 0) {
                queue.push(next);
            }
        }
    }

    return order.length === indegree.size ? order.join('') : '';
};
