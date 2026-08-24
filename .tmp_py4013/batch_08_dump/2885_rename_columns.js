// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/

/**
 * @param {object[]} students
 * @return {object[]}
 */
var renameColumns = function(students) {
    return students.map((r) => {
        if (Array.isArray(r)) {
            return { student_id: r[0], first_name: r[1], last_name: r[2], age_in_years: r[3] };
        }
        return {
            student_id: r.id,
            first_name: r.first,
            last_name: r.last,
            age_in_years: r.age,
        };
    });
};
