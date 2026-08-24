# LeetCode 2296 - Design a Text Editor
# https://leetcode.com/problems/design-a-text-editor/

class TextEditor
  def initialize
    @left = []
    @right = []
  end

  def add_text(text)
    text.each_char { |c| @left << c }
    nil
  end

  def delete_text(k)
    deleted = 0
    while k > 0 && !@left.empty?
      @left.pop
      k -= 1
      deleted += 1
    end
    deleted
  end

  def cursor_left(k)
    while k > 0 && !@left.empty?
      @right << @left.pop
      k -= 1
    end
    suffix
  end

  def cursor_right(k)
    while k > 0 && !@right.empty?
      @left << @right.pop
      k -= 1
    end
    suffix
  end

  private

  def suffix
    start = [0, @left.length - 10].max
    @left[start..].join
  end
end
