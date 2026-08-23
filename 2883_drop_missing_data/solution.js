// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

/**
 * @param {object[]} students
 * @return {object[]}
 */
var dropMissingData = function(students) {
    return students.filter((r) => {
        const name = Array.isArray(r) ? r[1] : r.name;
        return name !== null && name !== undefined && name !== '';
    });
};
