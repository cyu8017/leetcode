# LeetCode 2877 - Create a DataFrame from List
# https://leetcode.com/problems/create-a-dataframe-from-list/

# @param {Integer[][]} student_data
# @return {Object[]}
def create_dataframe(student_data)
  student_data.map { |student_id, age| { "student_id" => student_id, "age" => age } }
end
