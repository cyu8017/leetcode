// LeetCode 2877 - Create a DataFrame from List
// https://leetcode.com/problems/create-a-dataframe-from-list/

/**
 * @param {number[][]} studentData
 * @return {object[]}
 */
var createDataframe = function(studentData) {
    return studentData.map(([student_id, age]) => ({ student_id, age }));
};
