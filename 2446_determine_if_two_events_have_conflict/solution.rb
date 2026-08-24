# LeetCode 2446 - Determine if Two Events Have Conflict
# https://leetcode.com/problems/determine-if-two-events-have-conflict/

# @param {String[]} event1
# @param {String[]} event2
# @return {Boolean}
def have_conflict(event1, event2)
  event1[0] <= event2[1] && event2[0] <= event1[1]
end
