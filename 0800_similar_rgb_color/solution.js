// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

/**
 * @param {string} color
 * @return {string}
 */
var similarRGB = function(color) {
    const closest = (component) => {
        const value = parseInt(component, 16);
        const rounded = Math.floor((value + 8) / 17);
        const hex = rounded.toString(16);
        return hex + hex;
    };
    return "#" + closest(color.substring(1, 3)) + closest(color.substring(3, 5)) + closest(color.substring(5, 7));
};
