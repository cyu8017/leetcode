# LeetCode 1441 - Build An Array With Stack Operations
# https://leetcode.com/problems/build-an-array-with-stack-operations/

def build_array(target, n)
  answer = []
  current = 1
  target.each do |value|
    while current < value
      answer << 'Push' << 'Pop'
      current += 1
    end
    answer << 'Push'
    current += 1
  end
  answer
end
