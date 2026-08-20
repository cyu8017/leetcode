"use strict";
function destCity(paths) {
    const starts = new Set(paths.map((path) => path[0]));
    return paths.find((path) => !starts.has(path[1]))[1];
}
