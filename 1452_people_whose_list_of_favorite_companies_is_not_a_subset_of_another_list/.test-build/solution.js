"use strict";
function peopleIndexes(favoriteCompanies) { const sets = favoriteCompanies.map((x) => new Set(x)); return sets.map((set, i) => sets.every((other, j) => i === j || set.size > other.size || [...set].some((x) => !other.has(x))) ? i : -1).filter((i) => i >= 0); }
