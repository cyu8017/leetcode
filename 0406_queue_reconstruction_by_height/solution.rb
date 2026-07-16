# LeetCode 0406 - Queue Reconstruction by Height
# https://leetcode.com/problems/queue-reconstruction-by-height/

class Solution
  def reconstruct_queue(people)
    people.sort_by! { |person| [-person[0], person[1]] }
    queue = []
    people.each do |person|
      queue.insert(person[1], person)
    end
    queue
  end

  alias_method :reconstructQueue, :reconstruct_queue
end
