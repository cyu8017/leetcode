# LeetCode 1894 - Find the Student that Will Replace the Chalk
# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

# @param {Integer[]} chalk
# @param {Integer} k
# @return {Integer}
def chalk_replacer(chalk, k)
  k %= chalk.sum
  chalk.each_with_index do |need, index|
    return index if k < need

    k -= need
  end
  0
end
