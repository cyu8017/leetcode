// LeetCode 1418: Display Table Of Food Orders In A Restaurant

var displayTable = function(orders) {
    const foods = new Set(), tables = new Map();
    for (const [, table, food] of orders) { foods.add(food); if (!tables.has(table)) tables.set(table, new Map()); const row = tables.get(table); row.set(food, (row.get(food) || 0) + 1); }
    const menu = [...foods].sort(), result = [["Table", ...menu]];
    for (const table of [...tables.keys()].sort((a, b) => Number(a) - Number(b))) result.push([table, ...menu.map(food => String(tables.get(table).get(food) || 0))]);
    return result;
};
