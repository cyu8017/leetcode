# LeetCode 3450 - Maximum Students on a Single Bench
# https://leetcode.com/problems/maximum-students-on-a-single-bench/

# @param {Integer[][]} students
# @return {Integer}
def max_students_on_bench(students)
  bench = {}
  students.each do |s|
    bench[s[1]] ||= {}
    bench[s[1]][s[0]] = true
  end
  ans = 0
  bench.each_value do |st|
    ans = st.length if st.length > ans
  end
  ans
end
