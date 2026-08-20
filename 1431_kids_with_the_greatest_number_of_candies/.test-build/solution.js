"use strict";
function kidsWithCandies(candies, extraCandies) {
    const maximum = Math.max(...candies);
    return candies.map((x) => x + extraCandies >= maximum);
}
