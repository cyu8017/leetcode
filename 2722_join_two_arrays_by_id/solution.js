// LeetCode 2722 - Join Two Arrays by ID
// https://leetcode.com/problems/join-two-arrays-by-id/

var join = function(arr1, arr2) {
    const byId = new Map();
    for (const obj of arr1) byId.set(obj.id, { ...obj });
    for (const obj of arr2) {
        if (byId.has(obj.id)) Object.assign(byId.get(obj.id), obj);
        else byId.set(obj.id, { ...obj });
    }
    return [...byId.values()].sort((a, b) => a.id - b.id);
};
