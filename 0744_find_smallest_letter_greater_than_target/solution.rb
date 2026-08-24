# LeetCode 0744 - Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# @param {String[]} letters
# @param {Character} target
# @return {Character}
def next_greatest_letter(letters, target)
  left = 0
  right = letters.length
  while left < right
    mid = (left + right) / 2
    if letters[mid] <= target
      left = mid + 1
    else
      right = mid
    end
  end
  letters[left % letters.length]
end
