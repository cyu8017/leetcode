# LeetCode 1282 - Group the People Given the Group Size They Belong To
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

# @param {Integer[]} group_sizes
# @return {Integer[][]}
def group_the_people(group_sizes)
  pending = Hash.new { |h, k| h[k] = [] }
  answer = []
  group_sizes.each_with_index do |size, person|
    pending[size] << person
    if pending[size].length == size
      answer << pending[size]
      pending[size] = []
    end
  end
  answer.sort_by { |group| [group.length, group] }
end
